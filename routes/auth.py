from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user

from extensions import db
from models import User, AuditLog
from config import Config

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        fullname = request.form.get("fullname", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        error = None
        if not fullname or not email or not phone or not password:
            error = "Please fill in all fields."
        elif len(password) < 8:
            error = "Password must be at least 8 characters long."
        elif password != confirm:
            error = "Passwords do not match."
        elif User.query.filter_by(email=email).first():
            error = "An account with this email already exists."

        if error:
            flash(error, "error")
            return render_template("register.html", form=request.form)

        user = User(fullname=fullname, email=email, phone=phone)
        user.set_password(password)  # password is hashed, never stored in plain text
        db.session.add(user)
        db.session.commit()

        AuditLog.log("REGISTER", user=user, details="New account created",
                      ip_address=request.remote_addr)

        flash("Account created successfully. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form={})


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            AuditLog.log("LOGIN_FAILED", details=f"Failed login attempt for {email}",
                         ip_address=request.remote_addr)
            flash("Invalid email or password.", "error")
            return render_template("login.html")

        # Step 1 of 2 passed. Generate an OTP for MFA before granting a session.
        code = user.generate_otp(Config.OTP_LENGTH, Config.OTP_EXPIRY_SECONDS)
        db.session.commit()

        session["otp_pending_user_id"] = user.id
        # Demo-only: since there is no SMS/email gateway wired up, we show the
        # code directly on the verification screen instead of delivering it.
        session["demo_otp_code"] = code

        next_url = request.form.get("next") or request.args.get("next")
        if next_url:
            session["login_next_url"] = next_url

        AuditLog.log("LOGIN_OTP_SENT", user=user, details="OTP generated for MFA",
                      ip_address=request.remote_addr)

        return redirect(url_for("auth.verify_otp"))

    return render_template("login.html")


@auth_bp.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    pending_id = session.get("otp_pending_user_id")
    if not pending_id:
        flash("Please log in first.", "error")
        return redirect(url_for("auth.login"))

    user = User.query.get(pending_id)
    if not user:
        session.pop("otp_pending_user_id", None)
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        code = request.form.get("otp", "").strip()
        ok, message = user.verify_otp(code)
        db.session.commit()

        if ok:
            session.pop("otp_pending_user_id", None)
            session.pop("demo_otp_code", None)
            next_url = session.pop("login_next_url", None)
            login_user(user)
            AuditLog.log("LOGIN_SUCCESS", user=user, details="MFA verified",
                         ip_address=request.remote_addr)
            flash(f"Welcome back, {user.fullname.split()[0]}!", "success")
            return redirect(next_url or url_for("dashboard.dashboard"))
        else:
            AuditLog.log("LOGIN_OTP_FAILED", user=user, details=message,
                         ip_address=request.remote_addr)
            flash(message, "error")

    return render_template("verify_otp.html", demo_code=session.get("demo_otp_code"),
                            email=user.email)


@auth_bp.route("/resend-otp")
def resend_otp():
    pending_id = session.get("otp_pending_user_id")
    if not pending_id:
        return redirect(url_for("auth.login"))

    user = User.query.get(pending_id)
    if not user:
        return redirect(url_for("auth.login"))

    code = user.generate_otp(Config.OTP_LENGTH, Config.OTP_EXPIRY_SECONDS)
    db.session.commit()
    session["demo_otp_code"] = code

    AuditLog.log("LOGIN_OTP_RESENT", user=user, ip_address=request.remote_addr)
    flash("A new code has been generated.", "info")
    return redirect(url_for("auth.verify_otp"))


@auth_bp.route("/logout")
@login_required
def logout():
    AuditLog.log("LOGOUT", user=current_user, ip_address=request.remote_addr)
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.home"))
