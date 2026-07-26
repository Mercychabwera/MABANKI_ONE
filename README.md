# MABANKI-ONE

## FINOVATE 2026 Hackathon Project

### Team Name

binary minds

### University

lilongwe university of Agriculture and natural resources (LUARNA)
---

# Project Overview

Mabanki-One is a unified banking portal that allows users to access banking services from multiple banks through a single platform.
Instead of visiting different bank websites, users can compare products, learn about financial services, receive recommendations, and apply online in one place.

**"Building Student-Led Solutions for Banking, Payments and Financial Inclusion."**
---
# Problem Statement

Many people in Malawi find it difficult to compare banking products because information is spread across different banks.

Challenges include:

* Limited access to banking information
* Low financial literacy
* Time-consuming application processes
* Difficulty choosing suitable financial products
---

# Our Solution

Mabanki-One provides a single platform where users can:

* Compare banking products from different banks
* Learn financial concepts through simple educational content
* Get personalized recommendations
* Apply for banking services online
* Track application status
* Continue unfinished applications
* Access information in local languages

# Installation Guide

### Step 1: Open the Project Repository

Visit the project repository:

[MABANKI_ONE Repository](https://github.com/Mercychabwera/MABANKI_ONE?utm_source=chatgpt.com)

### Step 2: Download the Project

1. Click the green **Code** button.
2. Click **Download ZIP**.
3. Save the ZIP file to your computer.
4. Extract the ZIP file.

### Step 3: Open the Project Folder

Open the extracted **MABANKI_ONE** folder in Visual Studio Code.

### Step 4: Open Terminal

In VS Code:

* Click **Terminal**
* Click **New Terminal**

### Step 5: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 6: Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### Step 7: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 8: Run the Application

```bash
python app.py
```

### Step 9: Open the Application

After running the command above, open your web browser and go to:

```text
*http://127.0.0.1:5000**.
```
You should now see the Mabanki-One application running.
---
# Technologies Used

### Frontend
* HTML
* CSS
* Bootstrap

### Backend
* Python
* Flask

### Database
* SQLite
### Development Tools
* Git
* GitHub
* Visual Studio Code
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


### Step 7: Key Features
Multi-Bank Access

Users can view banking products from different banks in one place.

Product Comparison

Compare savings accounts, loans, and other banking products easily.

Financial Literacy Hub

Provides simple explanations of banking and financial topics.

Smart Recommendations

Suggests suitable banking products based on user needs.

Application Tracking

Allows users to check the progress of submitted applications.

Multi-Language Support

Available in:

English
Chichewa
Chitumbuka

Secure Login
Passwords are encrypted using industry-standard hashing methods.
Plain-text passwords are never stored.

OTP Verification
One-Time Passwords are used for additional account security.
OTP codes expire automatically after a short period.

User Privacy
Users can only access their own applications and documents.

Secure File Uploads
Uploaded documents are stored securely.
File names are automatically protected.

Audit Logging
Important system activities are recorded for security and monitoring purposes.
---
#Team Members and Roles

Jacqueline Kufeyani	Project Manager & Documentation Lead
Mercy Chabwera	Software Developer
Martha James	Presenter & Pitch Lead
Wezzie Muheka	Research Lead
Dines Nkumcheza	Business Strategist

# Future Improvements

* Mobile application
* USSD integration
* More bank partnerships
* AI-powered chatbot assistant
* Fraud detection features
* Open banking APIs
---
# Screenshots

Include screenshots of:

* Home Page
* Compare Banks Page
* Financial Literacy Page
* Recommendation Page
* Application Status Page
---

# Demo Video

Demo Link:

(To be added)
---

