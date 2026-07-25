"""
Lightweight, dependency-free i18n for Mabanki-One.

Rather than pulling in Flask-Babel (which needs a compiled .mo build step),
we keep a plain Python dictionary of {key: {lang: text}} pairs and a small
`t(key)` helper that is injected into every template as a Jinja global.

Supported languages:
    en   - English
    ny   - Chichewa
    tum  - Chitumbuka

NOTE: The Chichewa and Chitumbuka strings below are best-effort translations
for demo purposes. Before a production launch they should be reviewed by a
native speaker / professional translator, particularly the banking and
financial-literacy terminology.
"""

LANGUAGE_NAMES = {
    "en": "English",
    "ny": "Chichewa",
    "tum": "Chitumbuka",
}

TRANSLATIONS = {
    # ---- Brand / nav -------------------------------------------------
    "brand_tagline": {
        "en": "One Portal. Multiple Banks. Simple Account Opening.",
        "ny": "Portal Imodzi. Mabanki Ambiri. Kutsegula Akaunti Mosavuta.",
        "tum": "Portal Yimoza. Mabanki Ghanandi. Kujula Akaunti Mwambura Suzgo.",
    },
    "nav_home": {"en": "Home", "ny": "Kunyumba", "tum": "Kukaya"},
    "nav_compare": {"en": "Compare Banks", "ny": "Yerekezerani Mabanki", "tum": "Yaniskani Mabanki"},
    "nav_literacy": {"en": "Financial Literacy", "ny": "Maphunziro a Ndalama", "tum": "Kusambira za Ndalama"},
    "nav_dashboard": {"en": "My Applications", "ny": "Zofuna Zanga", "tum": "Vyakupempha Vyane"},
    "nav_login": {"en": "Log In", "ny": "Lowani", "tum": "Njilani"},
    "nav_register": {"en": "Register", "ny": "Lembetsani", "tum": "Njizgani"},
    "nav_logout": {"en": "Log Out", "ny": "Tulukani", "tum": "Fumani"},

    # ---- Home page -----------------------------------------------------
    "home_welcome": {"en": "Welcome", "ny": "Takulandirani", "tum": "Tamukwamukwa"},
    "home_intro": {
        "en": "Open a bank account online by comparing participating banks and choosing the one that best suits your needs.",
        "ny": "Tsegulani akaunti ya banki pa intaneti poyerekezera mabanki omwe akutenga nawo mbali ndikusankha yomwe ikukukwaniritsani bwino.",
        "tum": "Julani akaunti ya banki pa intaneti mwakuyaniska mabanki agho ghakuchita seŵera na kusankha ilo likukukwaniskani makora.",
    },
    "home_what_you_can_do": {"en": "What You Can Do", "ny": "Zomwe Mungachite", "tum": "Ivyo Mungachita"},
    "home_feature_compare": {"en": "Compare banks side by side.", "ny": "Yerekezerani mabanki mbali ndi mbali.", "tum": "Yaniskani mabanki side na side."},
    "home_feature_rates": {"en": "View savings and loan interest rates.", "ny": "Onani chiwongola dzanja cha akaunti ya sungani ndi ngongole.", "tum": "Wonani ma-interest gha kusunga na ngongoli."},
    "home_feature_choose": {"en": "Choose your preferred bank.", "ny": "Sankhani banki yomwe mukufuna.", "tum": "Sankhani banki yiyo mukukhumba."},
    "home_feature_apply": {"en": "Complete one simple online application.", "ny": "Malizani fomu imodzi yosavuta pa intaneti.", "tum": "Mazgani fomu yimoza yambura suzgo pa intaneti."},
    "home_feature_track": {"en": "Track your application from anywhere.", "ny": "Tsatirani mmene fomu yanu ikuyendera kulikonse.", "tum": "Landirani nkhani ya vyakupempha vyinu kulikose."},
    "home_start_btn": {"en": "Start Application", "ny": "Yambani Fomu", "tum": "Yambani Kupempha"},
    "home_learn_btn": {"en": "Learn About Money", "ny": "Phunzirani za Ndalama", "tum": "Sambirani za Ndalama"},

    # ---- Auth ------------------------------------------------------------
    "auth_login_title": {"en": "Log In", "ny": "Kulowa", "tum": "Kunjila"},
    "auth_register_title": {"en": "Create an Account", "ny": "Pangani Akaunti", "tum": "Panganiko Akaunti"},
    "auth_fullname": {"en": "Full Name", "ny": "Dzina Lonse", "tum": "Zina Lose"},
    "auth_email": {"en": "Email Address", "ny": "Imelo", "tum": "Imelo"},
    "auth_phone": {"en": "Phone Number", "ny": "Nambala ya Foni", "tum": "Nambara ya Foni"},
    "auth_password": {"en": "Password", "ny": "Mawu Achinsinsi", "tum": "Mazgu Ghakubisika"},
    "auth_confirm_password": {"en": "Confirm Password", "ny": "Tsimikizani Mawu Achinsinsi", "tum": "Simikizgani Mazgu Ghakubisika"},
    "auth_no_account": {"en": "Don't have an account?", "ny": "Mulibe akaunti?", "tum": "Mulije akaunti?"},
    "auth_have_account": {"en": "Already have an account?", "ny": "Muli ndi akaunti kale?", "tum": "Muli na akaunti kali?"},
    "auth_otp_title": {"en": "Enter Verification Code", "ny": "Lowetsani Nambala Yotsimikizira", "tum": "Njizgani Nambara Yakusimikizga"},
    "auth_otp_instructions": {
        "en": "For your security, we've generated a one-time code for this login. In this demo, it is shown below instead of being sent by SMS/email.",
        "ny": "Chifukwa cha chitetezo chanu, tapanga nambala imodzi yogwiritsa ntchito kamodzi. Pa demo iyi, ikuwonetsedwa pansipa m'malo motumizidwa pa SMS/imelo.",
        "tum": "Chifukwa cha usungilizi winu, tapangaso nambara yakugwiliskira kamoza pa kunjila uku. Pa demo iyi, yikulongoreka pasi m'malo mwakutuma pa SMS/imelo.",
    },
    "auth_otp_code_label": {"en": "Your one-time code (demo)", "ny": "Nambala yanu yakamodzi (demo)", "tum": "Nambara yinu yakamoza (demo)"},
    "auth_verify_btn": {"en": "Verify & Continue", "ny": "Tsimikizani ndi Pitirizani", "tum": "Simikizgani na Lutilirani"},
    "auth_resend_otp": {"en": "Resend Code", "ny": "Tumizaninso Nambala", "tum": "Tumaninizoso Nambara"},

    # ---- Dashboard ---------------------------------------------------
    "dash_title": {"en": "My Applications", "ny": "Zofuna Zanga", "tum": "Vyakupempha Vyane"},
    "dash_new_application": {"en": "Start New Application", "ny": "Yambani Fomu Yatsopano", "tum": "Yambani Kupempha Kupya"},
    "dash_no_apps": {"en": "You haven't started any applications yet.", "ny": "Simunayambe fomu iliyonse.", "tum": "Mundakwambepo kupempha kulikose."},
    "dash_resume": {"en": "Resume", "ny": "Pitirizani", "tum": "Lutilirani"},
    "dash_view": {"en": "View", "ny": "Onani", "tum": "Wonani"},
    "dash_status": {"en": "Status", "ny": "Mkhalidwe", "tum": "Umo Vilili"},
    "dash_bank": {"en": "Bank", "ny": "Banki", "tum": "Banki"},
    "dash_updated": {"en": "Last Updated", "ny": "Kusinthidwa Komaliza", "tum": "Kasindizgo Kaumaliro"},

    # ---- Application form ---------------------------------------------
    "app_form_title": {"en": "Application Form", "ny": "Fomu ya Zofuna", "tum": "Fomu ya Kupempha"},
    "app_national_id": {"en": "National ID Number", "ny": "Nambala ya Chitupa", "tum": "Nambara ya Chitupa"},
    "app_dob": {"en": "Date of Birth", "ny": "Tsiku Lobadwa", "tum": "Zuŵa Lakubabika"},
    "app_gender": {"en": "Gender", "ny": "Jenda", "tum": "Jenda"},
    "app_occupation": {"en": "Occupation", "ny": "Ntchito", "tum": "Nchito"},
    "app_address": {"en": "Physical Address", "ny": "Adilesi", "tum": "Adilesi"},
    "app_select_bank": {"en": "Select Bank", "ny": "Sankhani Banki", "tum": "Sankhani Banki"},
    "app_account_type": {"en": "Account Type", "ny": "Mtundu wa Akaunti", "tum": "Mtundu wa Akaunti"},
    "app_save_continue": {"en": "Save & Continue", "ny": "Sungani ndi Pitirizani", "tum": "Sungani na Lutilirani"},
    "app_back": {"en": "Back", "ny": "Bwererani", "tum": "Weleraniko"},

    # ---- Upload -----------------------------------------------------
    "upload_title": {"en": "Upload Required Documents", "ny": "Tumizani Zikalata Zofunika", "tum": "Tumizgani Vyoловka Vyakukhumbikwa"},
    "upload_id": {"en": "National ID Copy", "ny": "Kope la Chitupa", "tum": "Kopi ya Chitupa"},
    "upload_photo": {"en": "Passport Photo", "ny": "Chithunzi cha Pasipoti", "tum": "Chithuzi cha Pasipoti"},
    "upload_residence": {"en": "Proof of Residence", "ny": "Umboni wa Kukhala", "tum": "Ukaboni wa Kukhala"},
    "upload_employment": {"en": "Employment Letter (Optional)", "ny": "Kalata ya Ntchito (Osakakamiza)", "tum": "Kalata ya Nchito (Chikhumbo Waka)"},
    "upload_business": {"en": "Business Registration Certificate (Optional)", "ny": "Satifiketi ya Bizinesi (Osakakamiza)", "tum": "Satifiketi ya Bizinesi (Chikhumbo Waka)"},

    # ---- Review / success --------------------------------------------
    "review_title": {"en": "Review Your Details", "ny": "Onani Zambiri Zanu", "tum": "Wonani Fundo Zinu"},
    "review_submit": {"en": "Submit Application", "ny": "Tumizani Fomu", "tum": "Tumizgani Fomu"},
    "success_title": {"en": "Application Submitted Successfully!", "ny": "Fomu Yatumizidwa Bwino!", "tum": "Fomu Yatumizgika Makora!",},

    # ---- Common ----------------------------------------------------
    "footer_note": {"en": "MABANKI-ONE Prototype", "ny": "MABANKI-ONE Chitsanzo", "tum": "MABANKI-ONE Chiyelezgero"},
}


def t(key, lang="en"):
    """Translate `key` into `lang`, falling back to English, then the key itself."""
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key
    return entry.get(lang) or entry.get("en") or key
