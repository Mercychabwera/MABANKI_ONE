import os
import uuid

from flask import (
    Blueprint, render_template, request, redirect, url_for, flash,
    current_app, abort
)
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from extensions import db
from models import Application, Document, AuditLog
from content import BANKS

applications_bp = Blueprint("applications", __name__, url_prefix="/application")


def _get_owned_application(app_id):
    application = Application.query.get_or_404(app_id)
    if application.user_id != current_user.id:
        abort(403)
    return application


def _allowed_file(filename):
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return ext in current_app.config["ALLOWED_EXTENSIONS"]


@applications_bp.route("/new")
@login_required
def new_application():
    bank = request.args.get("bank", "")
    application = Application(
        user_id=current_user.id,
        bank_name=bank,
        full_name=current_user.fullname,
        phone=current_user.phone,
        email=current_user.email,
        status=Application.STATUS_DRAFT,
        current_step=Application.STEP_DETAILS,
    )
    db.session.add(application)
    db.session.commit()

    AuditLog.log("APPLICATION_CREATED", user=current_user,
                  details=f"Application #{application.id} started (bank={bank or 'not chosen'})",
                  ip_address=request.remote_addr)

    return redirect(url_for("applications.details", app_id=application.id))


@applications_bp.route("/<int:app_id>/resume")
@login_required
def resume(app_id):
    application = _get_owned_application(app_id)
    step_routes = {
        Application.STEP_DETAILS: "applications.details",
        Application.STEP_DOCUMENTS: "applications.upload",
        Application.STEP_REVIEW: "applications.review",
        Application.STEP_SUBMITTED: "applications.success",
    }
    target = step_routes.get(application.current_step, "applications.details")
    return redirect(url_for(target, app_id=application.id))


@applications_bp.route("/<int:app_id>/details", methods=["GET", "POST"])
@login_required
def details(app_id):
    application = _get_owned_application(app_id)

    if request.method == "POST":
        application.full_name = request.form.get("fullname", "").strip()
        application.national_id = request.form.get("national_id", "").strip()
        application.dob = request.form.get("dob", "").strip()
        application.gender = request.form.get("gender", "").strip()
        application.phone = request.form.get("phone", "").strip()
        application.email = request.form.get("email", "").strip()
        application.occupation = request.form.get("occupation", "").strip()
        application.address = request.form.get("address", "").strip()
        application.bank_name = request.form.get("bank", "").strip()
        application.account_type = request.form.get("account_type", "").strip()

        application.current_step = max(application.current_step, Application.STEP_DOCUMENTS)
        db.session.commit()

        AuditLog.log("APPLICATION_DETAILS_SAVED", user=current_user,
                      details=f"Application #{application.id} details saved",
                      ip_address=request.remote_addr)

        return redirect(url_for("applications.upload", app_id=application.id))

    return render_template("application.html", application=application, banks=BANKS)


@applications_bp.route("/<int:app_id>/upload", methods=["GET", "POST"])
@login_required
def upload(app_id):
    application = _get_owned_application(app_id)

    if request.method == "POST":
        required = {"idcopy": "National ID", "photo": "Passport Photo", "residence": "Proof of Residence"}
        optional = {"employment": "Employment Letter", "business": "Business Registration"}

        for field, missing_label in required.items():
            file = request.files.get(field)
            if not file or file.filename == "":
                flash(f"{missing_label} is required.", "error")
                return render_template("upload.html", application=application)
            if not _allowed_file(file.filename):
                flash(f"{missing_label}: only PDF, PNG or JPG files are allowed.", "error")
                return render_template("upload.html", application=application)

        upload_dir = os.path.join(current_app.config["UPLOAD_FOLDER"],
                                   str(current_user.id), str(application.id))
        os.makedirs(upload_dir, exist_ok=True)

        all_fields = {**required, **optional}
        for field, doc_type in all_fields.items():
            file = request.files.get(field)
            if not file or file.filename == "":
                continue
            if not _allowed_file(file.filename):
                continue

            original = secure_filename(file.filename)
            ext = original.rsplit(".", 1)[-1].lower()
            stored_name = f"{field}_{uuid.uuid4().hex[:10]}.{ext}"
            file.save(os.path.join(upload_dir, stored_name))

            doc = Document(
                application_id=application.id,
                doc_type=doc_type,
                original_filename=original,
                stored_filename=stored_name,
            )
            db.session.add(doc)

        application.current_step = max(application.current_step, Application.STEP_REVIEW)
        db.session.commit()

        AuditLog.log("APPLICATION_DOCS_UPLOADED", user=current_user,
                      details=f"Documents uploaded for application #{application.id}",
                      ip_address=request.remote_addr)

        return redirect(url_for("applications.review", app_id=application.id))

    return render_template("upload.html", application=application)


@applications_bp.route("/<int:app_id>/review")
@login_required
def review(app_id):
    application = _get_owned_application(app_id)
    return render_template("review.html", application=application)


@applications_bp.route("/<int:app_id>/submit", methods=["POST"])
@login_required
def submit(app_id):
    from datetime import datetime

    application = _get_owned_application(app_id)
    application.status = Application.STATUS_SUBMITTED
    application.current_step = Application.STEP_SUBMITTED
    application.submitted_at = datetime.utcnow()
    db.session.commit()

    AuditLog.log("APPLICATION_SUBMITTED", user=current_user,
                  details=f"Application #{application.id} submitted to {application.bank_name}",
                  ip_address=request.remote_addr)

    return redirect(url_for("applications.success", app_id=application.id))


@applications_bp.route("/<int:app_id>/success")
@login_required
def success(app_id):
    application = _get_owned_application(app_id)
    return render_template("success.html", application=application)
