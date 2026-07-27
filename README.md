MABANKI-ONE
FINOVATE 2026 Hackathon Project

Team Name: Binary minds

University: Lilongwe University of Agriculture and  Natural Resources (LUANAR)

Project Overview:
Mabanki-One is a unified banking portal that allows users to access banking services from multiple banks through a single platform. Instead of visiting different bank websites, users can compare products, learn about financial services, receive recommendations and apply online in one place.

"Building Student-Led Solutions for Banking, Payments and Financial Inclusion."

Problem Statement:
Many people in Malawi find it difficult to compare banking products because information is spread across different banks.

Challenges include:
✓. Limited access to banking information
Low financial literacy
✓. Time-consuming application processes
✓. Difficulty choosing suitable financial products
Suggested Solution
Mabanki-One provides a single platform where users can:
✓. Compare banking products from different banks
✓. Learn financial concepts through simple educational content
✓. Get personalized recommendations
✓. Apply for banking services online
✓. Track application status
✓. Continue unfinished applications 
✓. Access information in local languages

Installation Guide:
✓. Step 1: Open the Project Repository
and then visit the project repository:

"MABANKI_ONE Repository"

✓. Step 2: Download the Project
=> Click on the green Code button.
=> Click Download ZIP.
=> Save the ZIP file to your computer.
=> Extract the ZIP file.
✓. Step 3: Open the Project Folder
=> Open the extracted "MABANKI_ONE" folder in Visual Studio Code.

✓. Step 4: Open Terminal in VS Code:
=> Click Terminal
=> Click New Terminal
✓. Step 5: Create a Virtual Environment
python -m venv venv
✓. Step 6: Activate the Virtual Environment
venv\Scripts\activate
✓. Step 7: Install Required Packages
 pip install -r requirements.txt 
✓. Step 8: Run the Application
 python app.py 
✓. Step 9: Open the Application.
After running the command above, open your web browser and go to:

http://127.0.0.1:5000

You will now see the Mabanki-One application running.

Technologies Used:
Frontend
HTML
CSS
Bootstrap
Backend
Python
Flask
Database
SQLite
Development Tools
Git
GitHub
Visual Studio Code
🗂️ Project structure
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
Step 7: Key Features
Multi-Bank Access

Users can view banking products from different banks in one place.

Product Comparison:
✓. Compare savings accounts, loans, and other banking products easily.

Financial Literacy Hub:
✓. Provides simple explanations of banking and financial topics.

Smart Recommendations:
✓. Suggests suitable banking products based on user needs.

Application Tracking:
✓. Allow users to check the progress of submitted applications.

Multi-Language Support
✓. Available both in:
=> English, Chichewa and Chitumbuka

Secure Login: 
✓. Passwords are encrypted using industry-standard hashing methods. 
✓. Plain-text passwords are not permitted. 

OTP Verification: ✓.One-Time Passwords are used for additional account security and OTP codes expire automatically after a short period.

User Privacy Users can only access their own applications and documents.

Secure File Uploads: ✓. Uploaded documents are stored securely. 
✓. File names are automatically protected.

Audit Logging: ✓.Important system activities are recorded for security and monitoring purposes.

 Team Members and Roles: 
1. Jacqueline Kufeyani: Project Manager & Documentation Lead 
2. Mercy Chabwera: Software Developer 
3. Martha James: Presenter & Pitch Lead 
4. Wezzie Muheka: Research Lead
5. Dines Nkumcheza: Business Strategist

Future Improvements:
✓. Mobile application
✓. USSD integration
✓. More bank partnerships
✓. AI-powered chatbot assistant
✓. Fraud detection features

Business Model Summary
  
MABANKI-ONE

1. Problem Statement  
Many people face several challenges when opening a bank account. These include:  
- Limited access to banking information – Many people do not know the requirements or steps for opening an account.  
- Low financial literacy – Some customers struggle to understand different account types and banking services.  
- Time-consuming application process – Customers spend a lot of time travelling to bank branches filling out paper forms and waiting in long queues.  
- Difficulty choosing suitable financial products – Customers may not know which account best suits their needs.  
- Language barriers – Some customers cannot easily understand banking information because it is not available in their preferred language.  

These challenges make banking less accessible especially for first-time users and people living far from bank branches.

2. Target Users  
Our solution is designed for:  
Students  
Working professionals  
Small business owners  
First-time bank customers  
People in rural and urban areas  
Banks that want to improve customer service and reduce paperwork

3. Value Proposition  
Binary Minds – Scan & Sign offers a secure simple and paperless way to open a bank account.  
Our solution provides:  
- Online account opening from anywhere  
- ID scanning for faster data capture  
- Electronic signature for paperless applications  
- Clear information about banking products  
- Multiple language support to reduce language barriers  
- A faster and more convenient customer experience  
- Reduced paperwork and lower operational costs for banks

4. How the Project Could Be Sustained or Generate Value  
The project can generate value by:  
- Allowing banks to subscribe to or license the platform  
- Reducing printing storage and administrative costs  
- Helping banks process more applications in less time  
- Improving customer satisfaction which can attract more customers  
- Expanding the platform to serve multiple banks in Malawi and beyond

5ncial literacy  
- Personalised account recommendations based on customer needs
