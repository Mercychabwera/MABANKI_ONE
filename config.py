import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # NOTE: For the FINOVATE demo this key is generated once at import time.
    # In a real deployment, set SECRET_KEY as an environment variable instead.
    SECRET_KEY = os.environ.get("SECRET_KEY", "mabanki-one-demo-secret-change-me")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "instance", "mabanki.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8MB per request

    # OTP settings (demo mode: code is shown on screen / flashed instead of
    # being sent through a real SMS/email gateway)
    OTP_LENGTH = 6
    OTP_EXPIRY_SECONDS = 300  # 5 minutes

    LANGUAGES = ["en", "ny", "tum"]
    DEFAULT_LANGUAGE = "en"
