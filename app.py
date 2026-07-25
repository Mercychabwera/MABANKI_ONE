import os
import click
from flask import Flask, session, request
from flask_login import current_user

from config import Config
from extensions import db, login_manager
from models import User, AuditLog
from translations import t, LANGUAGE_NAMES


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # --- Extensions -----------------------------------------------------------
    db.init_app(app)
    login_manager.init_app(app)

    # --- User loader for Flask-Login ------------------------------------------
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # --- Before-request: set up language and context for every template -------
    @app.before_request
    def set_globals():
        lang = session.get("lang", Config.DEFAULT_LANGUAGE)
        # If user is logged in, their preferred language can override the session
        if current_user.is_authenticated and "lang" not in session:
            lang = current_user.preferred_language or Config.DEFAULT_LANGUAGE
        session["lang"] = lang

        # These will be available via app.context_processor below
        app.config["_lang"] = lang

    @app.context_processor
    def inject_i18n():
        lang = app.config.get("_lang", Config.DEFAULT_LANGUAGE)
        return {
            "t": lambda key: t(key, lang),
            "current_lang": lang,
            "languages": Config.LANGUAGES,
            "language_names": LANGUAGE_NAMES,
        }

    # --- Register Blueprints --------------------------------------------------
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.applications import applications_bp
    from routes.dashboard import dashboard_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(applications_bp)
    app.register_blueprint(dashboard_bp)

    # --- CLI Commands ---------------------------------------------------------
    @app.cli.command("init-db")
    def init_db():
        """Create all database tables."""
        import sqlalchemy as sa
        inspector = sa.inspect(db.engine)
        existing = inspector.get_table_names()
        with app.app_context():
            db.create_all()
        created = [t for t in db.metadata.tables.keys() if t not in existing]
        if created:
            print(f"Created tables: {', '.join(created)}")
        else:
            print("All tables already exist.")

    @app.cli.command("create-admin")
    @click.argument("email")
    @click.argument("password")
    @click.option("--fullname", default="Admin User", help="Display name")
    def create_admin(email, password, fullname):
        """Create an admin user via CLI.
        
        Usage: flask create-admin <email> <password> [--fullname <name>]
        """
        with app.app_context():
            existing = User.query.filter_by(email=email).first()
            if existing:
                click.echo(f"User {email} already exists. Aborting.")
                return
            user = User(
                fullname=fullname,
                email=email,
                phone="0000000000",
                is_admin=True,
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            click.echo(f"Admin user created: {email}")
            AuditLog.log("ADMIN_CREATED", user=user,
                          details="Admin account created via CLI",
                          ip_address="127.0.0.1")

    # --- Create tables on first request (for convenience) ---------------------
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

