from flask import Blueprint, render_template, abort, request
from flask_login import login_required, current_user

from models import Application, AuditLog

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    applications = (
        Application.query.filter_by(user_id=current_user.id)
        .order_by(Application.updated_at.desc())
        .all()
    )
    return render_template("dashboard.html", applications=applications)


@dashboard_bp.route("/my-activity")
@login_required
def my_activity():
    logs = (
        AuditLog.query.filter_by(user_id=current_user.id)
        .order_by(AuditLog.timestamp.desc())
        .limit(100)
        .all()
    )
    return render_template("activity.html", logs=logs, scope="mine")


@dashboard_bp.route("/admin/audit-log")
@login_required
def admin_audit_log():
    if not current_user.is_admin:
        abort(403)

    page = request.args.get("page", 1, type=int)
    pagination = AuditLog.query.order_by(AuditLog.timestamp.desc()).paginate(
        page=page, per_page=50, error_out=False
    )
    return render_template("activity.html", logs=pagination.items, scope="all",
                            pagination=pagination)
