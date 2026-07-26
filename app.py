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