# MABANKI‑ONE

**One Portal. Multiple Banks. Simple Account Opening.**

MABANKI‑ONE is a prototype web portal that lets someone in Malawi compare
participating banks, learn the basics of personal finance, and complete a
single online application — including KYC document upload — to open an
account with the bank of their choice.

## problem
Many people find it difficult to compare banking products from different banks. They have to visit multiple bank branches or websites to find information about loans, savings accounts, and other services.

Many customers also do not understand banking terms such as interest rates, processing fees, and repayment periods.

This makes it difficult to make good financial decisions.
## Solution

MABANKI ONE is a Unified Multi-Bank Banking Portal that allows customers to access services from multiple banks using one platform.

The system helps users:
- Compare banking products
- Learn financial concepts
- Apply for services online
- Upload required documents
- Track applications
- Continue applications later if they leave before finishing
## Main Features

### Language Selection
Users can choose:

- English
- Chichewa
- Chitumbuka

### User Registration
Users create one account and access services through the portal.

### Compare Banking Products
Users can compare:

- Loans
- Savings Accounts
- Current Accounts

### Financial Literacy
The system explains banking terms such as:

- Interest Rate
- Processing Fee
- Monthly Payment

### Smart Recommendation
The system recommends the best product based on user information.

### Digital KYC
Users can upload:

- National ID
- Passport Photo
- Other supporting documents

### Application Tracking
Users can see if their application is:

- Submitted
- Under Review
- Approved
- Rejected

### Save and Resume
Users can continue an application from where they stopped.

---

## Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Mercychabwera/MABANKI_ONE.git
```

### 2. Open Project Folder

```bash
cd MABANKI_ONE
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Project

```bash
python app.py
```

### 7. Open Browser

```text
http://127.0.0.1:5000
```
---
## Demo Flow

1. Select Language
2. Register Account
3. Login
4. Choose Financial Goal
5. Compare Products
6. Read Financial Literacy Tips
7. Get Recommendation
8. Upload Documents
9. Submit Application
10. Track Application Status

## Team Members

- Jacqueline Kufeyani – Documentation & Presentation
- Mercy Chabwera – Backend Development
- martha – Frontend Development
- wezzie  muheka Member – UI/UX & Testing

--## Screenshots
Include screenshots of:

- Home Page
- Login Page
- Registration Page
- Product Comparison Page
- Dashboard
- KYC Upload Page

## ⚠️ Demo-mode notes (read this before judging)

This is a **hackathon prototype**, not a production banking system:

- **OTP delivery is simulated.** There is no SMS/email gateway wired up, so
  the one-time code is shown directly on the verification screen (clearly
  labeled "DEMO MODE") instead of being texted/emailed. Swapping in a real
  provider (e.g. an SMS aggregator operating in Malawi) only requires
  replacing the `session["demo_otp_code"]` line in `routes/auth.py` with an
  actual send call.
- **Bank approval is simulated.** Submitted applications move to
  "Submitted" status; there's no real integration with any bank's core
  banking system.
- **Chichewa/Chitumbuka translations** in `translations.py` and
  `content.py` are a best-effort pass for the demo and should be reviewed
  by a native speaker before any real deployment.
- **SQLite** is used for simplicity. For production, swap
  `SQLALCHEMY_DATABASE_URI` in `config.py` for a managed Postgres/MySQL
  instance.

---

## 🗂️ Project structure

```
mabanki-one/
├── app.py                 # App factory, blueprint registration, i18n wiring, CLI commands
├── config.py               # Configuration (secret key, DB URI, upload limits, languages)
├── extensions.py            # Shared Flask extension instances (db, login_manager)
├── models.py                # SQLAlchemy models: User, Application, Document, AuditLog
├── translations.py          # UI string dictionary for en / ny / tum + t() helper
├── content.py                # Bank list + financial literacy tips (per language)
├── requirements.txt
├── routes/
│   ├── main.py               # Home, language switch, bank comparison, literacy
│   ├── auth.py                # Register, login, OTP verification, logout
│   ├── applications.py        # Application wizard: details → upload → review → submit
│   └── dashboard.py           # "My Applications" dashboard + audit log views
├── templates/                # Jinja2 templates (one per page)
├── static/css/style.css        # Single stylesheet, CSS variables for theming
├── uploads/                   # KYC files land here, namespaced per user/application
└── instance/                  # SQLite database file lives here (auto-created)
```

---

## 🚀 Running it locally

**Requirements:** Python 3.10+

```bash
# 1. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialise the database (creates instance/mabanki.db)
export FLASK_APP=app.py          # Windows (PowerShell): $env:FLASK_APP="app.py"
flask init-db

# 4. (Optional) create an admin account so you can view the full audit log
flask create-admin admin@mabanki.mw "AStrongPassword123" --fullname "Demo Admin"

# 5. Run the app
python app.py
```

The site will be available at **http://127.0.0.1:5000**.

> The database also auto-creates itself the first time `app.py` runs, so
> step 3 is optional — it's there mainly if you want a clean DB before a
> demo.

---

## 🧭 Demo flow (suggested walkthrough for judges)

1. **Home (`/`)** — switch the language selector in the header between
   English / Chichewa / Chitumbuka and note the page updates.
2. **Compare Banks (`/select-bank`)** — see savings/loan rates side by
   side for six Malawian banks.
3. **Financial Literacy (`/literacy`)** — browse the short, translated
   tips on saving, interest rates, budgeting, debt, and KYC.
4. **Register (`/register`)** — create an account; note the password is
   never stored or shown in plain text.
5. **Log in (`/login`)** — enter your credentials, then land on the
   **OTP screen**. In demo mode the 6-digit code is shown right there
   (labelled DEMO MODE) — enter it to complete MFA sign-in.
6. **Open an account** — from the bank comparison table, click "Open
   Account" on any bank. Fill in the details form, upload the required
   KYC documents (any PDF/PNG/JPG works for the demo), review the summary,
   and submit.
7. **Save-and-resume** — start a second application, fill in the details
   step, then navigate away (e.g. to Home) without finishing. Go to
   **My Applications (`/dashboard`)** — the draft is waiting there with a
   "Resume" button that drops you back exactly where you left off.
8. **Track applications** — the dashboard shows a status badge (Draft /
   Submitted) and progress bar for every application you've started.
9. **Audit trail** — open the account menu → **Activity Log** to see your
   own security history (registration, sign-ins, OTP events, submissions).
   If you created an admin account in step 4 of setup, log in as that
   admin and open **Admin: Audit Log** from the account menu to see the
   full, system-wide log.

---

## 🔒 Security notes

- Passwords are hashed with Werkzeug's `generate_password_hash` (PBKDF2)
  — plaintext passwords are never stored or logged.
- OTP codes are hashed before being stored and expire after 5 minutes;
  a maximum of 5 verification attempts is enforced per code.
- Every application and document is scoped to the owning user; attempting
  to view another user's application returns `403 Forbidden`.
- Uploaded files are renamed with a random suffix on save and stored
  outside of any publicly served static path.
- All sensitive actions are written to the audit log with a timestamp,
  actor, and originating IP address.

---

## 🛣️ Possible next steps

- Wire up a real SMS/email provider for OTP delivery.
- Add a bank-facing dashboard so participating banks can review and
  action applications directly (approve / reject / request more info).
- Move file storage to object storage (e.g. S3-compatible) for
  production deployments.
- Add automated tests (pytest) around the auth and application flows.

---

*MABANKI‑ONE — built in Lilongwe, Malawi, for the FINOVATE Challenge.*
