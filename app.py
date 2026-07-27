<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

banks = [
    {
        "name": "National Bank of Malawi",
        "savings": "10% per year",
        "loan": "24% per year",
        "opening": "MK5,000"
    },
    {
        "name": "Standard Bank Malawi",
        "savings": "9% per year",
        "loan": "22% per year",
        "opening": "MK10,000"
    },
    {
        "name": "FDH Bank",
        "savings": "8% per year",
        "loan": "20% per year",
        "opening": "MK2,000"
    },
    {
        "name": "NBS Bank",
        "savings": "9.5% per year",
        "loan": "23% per year",
        "opening": "MK5,000"
    }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/select-bank")
def select_bank():
    return render_template("compare_banks.html", banks=banks)


@app.route("/application")
def application():
    return render_template("application.html")


@app.route("/review", methods=["POST"])
def review():

    fullname = request.form["fullname"]
    phone = request.form["phone"]
    email = request.form["email"]
    bank = request.form["bank"]
    account = request.form["account"]

    return render_template(
        "review.html",
        fullname=fullname,
        phone=phone,
        email=email,
        bank=bank,
        account=account
    )


@app.route("/success", methods=["POST"])
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
=======
import os
import click
from flask import Flask, session, request

from config import Config
from extensions import db, login_manager
from translations import t as translate, LANGUAGE_NAMES


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    os.makedirs(os.path.join(app.root_path, "instance"), exist_ok=True)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ---- blueprints -----------------------------------------------------
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.applications import applications_bp
    from routes.dashboard import dashboard_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(applications_bp)
    app.register_blueprint(dashboard_bp)

    # ---- i18n: pick language + expose t() to Jinja -----------------------
    @app.before_request
    def resolve_language():
        if "lang" not in session:
            session["lang"] = app.config["DEFAULT_LANGUAGE"]

    @app.context_processor
    def inject_i18n():
        lang = session.get("lang", app.config["DEFAULT_LANGUAGE"])
        return {
            "t": lambda key: translate(key, lang),
            "current_lang": lang,
            "languages": app.config["LANGUAGES"],
            "language_names": LANGUAGE_NAMES,
        }

    # ---- error pages ------------------------------------------------------
    @app.errorhandler(403)
    def forbidden(e):
        return ("<h1>403 - Forbidden</h1><p>You don't have permission to view this.</p>"
                "<a href='/'>Go home</a>"), 403

    @app.errorhandler(404)
    def not_found(e):
        return ("<h1>404 - Not Found</h1><p>That page doesn't exist.</p>"
                "<a href='/'>Go home</a>"), 404

    # ---- CLI helpers --------------------------------------------------
    @app.cli.command("init-db")
    def init_db():
        """Create all database tables."""
        db.create_all()
        click.echo("Database tables created.")

    @app.cli.command("create-admin")
    @click.argument("email")
    @click.argument("password")
    @click.option("--fullname", default="Mabanki Admin")
    @click.option("--phone", default="0000000000")
    def create_admin(email, password, fullname, phone):
        """Create (or promote) an admin user, e.g.:
        flask create-admin admin@mabanki.mw StrongPass123 --fullname "Admin"
        """
        user = User.query.filter_by(email=email.lower()).first()
        if user:
            user.is_admin = True
            click.echo(f"Existing user {email} promoted to admin.")
        else:
            user = User(fullname=fullname, email=email.lower(), phone=phone, is_admin=True)
            user.set_password(password)
            db.session.add(user)
            click.echo(f"Admin user {email} created.")
        db.session.commit()

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> a89820d0643d41027ff18f29b8182b32c6ffdcb3
