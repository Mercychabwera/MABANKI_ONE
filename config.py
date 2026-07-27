import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Secret key for Flask sessions and security
    # For production, store this as an environment variable
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "mabanki-one-demo-secret-change-me"
    )

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "instance", "mabanki.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # File upload settings (KYC documents)
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    ALLOWED_EXTENSIONS = {
        "pdf",
        "png",
        "jpg",
        "jpeg"
    }

    MAX_CONTENT_LENGTH = 8 * 1024 * 1024   # Maximum upload size: 8MB


    # OTP verification settings
    # Demo mode: OTP is displayed on screen instead of sending SMS/email

    OTP_LENGTH = 6
    OTP_EXPIRY_SECONDS = 300   # OTP expires after 5 minutes


    # Language settings
    # English, Chichewa, Chitumbuka

    LANGUAGES = [
        "en",
        "ny",
        "tum"
    ]

    DEFAULT_LANGUAGE = "en"