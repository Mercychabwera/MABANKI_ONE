import secrets
from datetime import datetime, timedelta

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    preferred_language = db.Column(db.String(10), default="en")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # --- MFA (OTP) fields -------------------------------------------------
    # Demo-mode OTP: a fresh 6-digit code is generated on login and its hash
    # (never the raw code) is stored here together with an expiry time.
    otp_hash = db.Column(db.String(255), nullable=True)
    otp_expires_at = db.Column(db.DateTime, nullable=True)
    otp_attempts = db.Column(db.Integer, default=0)

    applications = db.relationship(
        "Application", backref="applicant", lazy=True, cascade="all, delete-orphan"
    )

    # --- password helpers ---------------------------------------------------
    def set_password(self, raw_password):
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password_hash, raw_password)

    # --- OTP helpers ---------------------------------------------------------
    def generate_otp(self, length=6, expiry_seconds=300):
        code = "".join(secrets.choice("0123456789") for _ in range(length))
        self.otp_hash = generate_password_hash(code)
        self.otp_expires_at = datetime.utcnow() + timedelta(seconds=expiry_seconds)
        self.otp_attempts = 0
        return code

    def verify_otp(self, code):
        if not self.otp_hash or not self.otp_expires_at:
            return False, "No OTP was requested. Please log in again."
        if datetime.utcnow() > self.otp_expires_at:
            return False, "This code has expired. Please request a new one."
        if self.otp_attempts >= 5:
            return False, "Too many attempts. Please request a new code."

        self.otp_attempts = (self.otp_attempts or 0) + 1
        if check_password_hash(self.otp_hash, code):
            self.otp_hash = None
            self.otp_expires_at = None
            self.otp_attempts = 0
            return True, "OK"
        return False, "Incorrect code. Please try again."

    def clear_otp(self):
        self.otp_hash = None
        self.otp_expires_at = None
        self.otp_attempts = 0

    def __repr__(self):
        return f"<User {self.email}>"


class Application(db.Model):
    __tablename__ = "applications"

    STATUS_DRAFT = "Draft"
    STATUS_SUBMITTED = "Submitted"
    STATUS_REVIEW = "Under Review"
    STATUS_APPROVED = "Approved"
    STATUS_REJECTED = "Rejected"

    # step tracker for save-and-resume
    STEP_DETAILS = 1
    STEP_DOCUMENTS = 2
    STEP_REVIEW = 3
    STEP_SUBMITTED = 4

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    bank_name = db.Column(db.String(150))
    account_type = db.Column(db.String(80))

    full_name = db.Column(db.String(150))
    national_id = db.Column(db.String(50))
    dob = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(150))
    occupation = db.Column(db.String(120))
    address = db.Column(db.String(255))

    status = db.Column(db.String(30), default=STATUS_DRAFT)
    current_step = db.Column(db.Integer, default=STEP_DETAILS)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    submitted_at = db.Column(db.DateTime, nullable=True)

    documents = db.relationship(
        "Document", backref="application", lazy=True, cascade="all, delete-orphan"
    )

    def progress_percent(self):
        total_steps = self.STEP_SUBMITTED
        return int((min(self.current_step, total_steps) / total_steps) * 100)


class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("applications.id"), nullable=False)
    doc_type = db.Column(db.String(80))
    original_filename = db.Column(db.String(255))
    stored_filename = db.Column(db.String(255))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)


class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    action = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(500))
    ip_address = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User")

    @staticmethod
    def log(action, user=None, details="", ip_address=None):
        entry = AuditLog(
            user_id=user.id if user else None,
            action=action,
            details=details,
            ip_address=ip_address,
        )
        db.session.add(entry)
        db.session.commit()
        return entry
