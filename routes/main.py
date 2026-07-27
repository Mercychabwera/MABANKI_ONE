from flask import Blueprint, render_template, session, redirect, url_for, request

from content import BANKS, LITERACY_TIPS, GLOSSARY_TERMS, get_bank_badges
from config import Config

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/set-language/<lang_code>")
def set_language(lang_code):
    if lang_code in Config.LANGUAGES:
        session["lang"] = lang_code
    # Send the user back where they came from instead of always to "/"
    return redirect(request.referrer or url_for("main.home"))


@main_bp.route("/select-bank")
def select_bank():
    badges = get_bank_badges(BANKS)
    return render_template("compare_banks.html", banks=BANKS, badges=badges)


@main_bp.route("/literacy")
def literacy():
    return render_template("literacy.html", tips=LITERACY_TIPS, glossary=GLOSSARY_TERMS)
