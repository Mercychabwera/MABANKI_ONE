"""Static content used by the app: participating banks, bank-comparison
helpers, financial literacy tips and a short glossary, each provided in
English, Chichewa and Chitumbuka.

NOTE: Rates and fees below are indicative sample figures for the FINOVATE
demo only — not live product data from the banks named."""

# ---------------------------------------------------------------------------
# Bank comparison data
# ---------------------------------------------------------------------------
# savings_rate / loan_rate are annual percentages (numeric, for sorting).
# processing_fee / monthly_fee are in Malawi Kwacha (numeric, for sorting).
# digital_services is a short list of channels the bank offers.
BANKS = [
    {
        "name": "FDH Bank",
        "initials": "FDH",
        "logo_color": "#c1440e",
        "savings_rate": 8.0,
        "loan_rate": 19.0,
        "processing_fee": 15000,
        "monthly_fee": 500,
        "digital_services": ["Mobile Banking App", "USSD Banking (*247#)", "Internet Banking"],
    },
    {
        "name": "National Bank of Malawi",
        "initials": "NBM",
        "logo_color": "#0f5c50",
        "savings_rate": 10.5,
        "loan_rate": 24.0,
        "processing_fee": 20000,
        "monthly_fee": 1500,
        "digital_services": ["NBM Mobile App", "Internet Banking", "USSD Banking", "NBM Online"],
    },
    {
        "name": "Standard Bank Malawi",
        "initials": "SBM",
        "logo_color": "#0033a0",
        "savings_rate": 9.0,
        "loan_rate": 22.0,
        "processing_fee": 30000,
        "monthly_fee": 2500,
        "digital_services": ["Standard Bank App", "Internet Banking", "OneWallet Mobile Money"],
    },
    {
        "name": "NBS Bank",
        "initials": "NBS",
        "logo_color": "#1c6ea4",
        "savings_rate": 9.5,
        "loan_rate": 21.0,
        "processing_fee": 10000,
        "monthly_fee": 300,
        "digital_services": ["NBS Pay App", "Internet Banking", "USSD Banking (*247#)"],
    },
    {
        "name": "Ecobank Malawi",
        "initials": "ECO",
        "logo_color": "#003a70",
        "savings_rate": 9.2,
        "loan_rate": 22.5,
        "processing_fee": 22000,
        "monthly_fee": 1800,
        "digital_services": ["Ecobank Mobile App", "Internet Banking", "Rapid Transfer"],
    },
]


def get_bank_badges(banks=BANKS):
    """Return {bank_name: [badge_key, ...]} for the standout bank(s) in
    each category: lowest loan rate, highest savings rate, and lowest
    combined (processing + monthly) fees."""
    if not banks:
        return {}

    best_loan = min(banks, key=lambda b: b["loan_rate"])
    best_savings = max(banks, key=lambda b: b["savings_rate"])
    best_fees = min(banks, key=lambda b: b["processing_fee"] + b["monthly_fee"])

    badges = {}
    for bank_name, badge_key in (
        (best_loan["name"], "best_loans"),
        (best_savings["name"], "best_savings"),
        (best_fees["name"], "lowest_fees"),
    ):
        badges.setdefault(bank_name, []).append(badge_key)
    return badges


# ---------------------------------------------------------------------------
# Financial literacy glossary (side panel)
# ---------------------------------------------------------------------------
GLOSSARY_TERMS = [
    {
        "term": {"en": "Interest Rate", "ny": "Chiwongola Dzanja", "tum": "Interest"},
        "definition": {
            "en": "The percentage a bank pays you on savings, or charges you on a loan, usually expressed per year.",
            "ny": "Chiŵerengero cha peresenti chomwe banki imakulipirani pa akaunti ya sungani, kapena imakulipiritsani pa ngongole, nthawi zambiri pa chaka.",
            "tum": "Chiŵerengero cha peresenti icho banki yikumulipilani pa kusunga, panji yikumulipiskani pa ngongoli, kanandi pa chaka.",
        },
    },
    {
        "term": {"en": "Savings Account", "ny": "Akaunti ya Kusunga", "tum": "Akaunti ya Kusunga"},
        "definition": {
            "en": "A bank account where you keep money safely and earn interest on the balance over time.",
            "ny": "Akaunti ya banki yomwe mumasungiramo ndalama bwinobwino ndikupezako chiwongola dzanja pa ndalama zomwe muli nazo.",
            "tum": "Akaunti ya banki iyo mukusungirapo ndalama makora na kupokelera interest pa ndalama izo muli nazo.",
        },
    },
    {
        "term": {"en": "Loan Tenure", "ny": "Nthawi Yobweza Ngongole", "tum": "Nyengo ya Kuwezga Ngongoli"},
        "definition": {
            "en": "The length of time you are given to fully repay a loan, for example 12, 24 or 36 months.",
            "ny": "Kutalika kwa nthawi komwe mwapatsidwa kuti mubweze ngongole yonse, mwachitsanzo miyezi 12, 24 kapena 36.",
            "tum": "Utali wa nyengo iyo mwapika kuti muwezge ngongoli yose, mwachiyelezgero myezi 12, 24 panji 36.",
        },
    },
    {
        "term": {"en": "Processing Fee", "ny": "Ndalama Yokonzera Fomu", "tum": "Ndalama ya Kunozgera Fomu"},
        "definition": {
            "en": "A one-off charge the bank takes for reviewing and setting up your account or loan application.",
            "ny": "Ndalama yolipirira kamodzi yomwe banki imalandira pofufuza ndi kukonzekera akaunti kapena kupempha ngongole kwanu.",
            "tum": "Ndalama yakulipila kamoza iyo banki yikupokelera pakusanda na kunozgera akaunti panji kupempha ngongoli kwinu.",
        },
    },
    {
        "term": {"en": "Collateral", "ny": "Chikole", "tum": "Chikole"},
        "definition": {
            "en": "Something of value (like land, a car, or a salary guarantee) that you pledge to the bank in case you fail to repay a loan.",
            "ny": "Chinthu chamtengo wapatali (monga munda, galimoto, kapena chitsimikizo cha malipiro) chomwe mumapereka ku banki ngati chikole pamene mungalephere kubweza ngongole.",
            "tum": "Chinthu chakuzirwa (nga vilaza, galimoto, panji ukaboni wa malipiro) icho mukupeleka ku banki nga chikole usange mungatondeke kuwezga ngongoli.",
        },
    },
]

# ---------------------------------------------------------------------------
# Financial literacy tips
# ---------------------------------------------------------------------------

LITERACY_TIPS = [
    {
        "icon": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M4 21V10l8-6 8 6v11"/><path d="M9 21v-6h6v6"/></svg>''',
        "title": {
            "en": "Why Open a Bank Account?",
            "ny": "Bwanji Kutsegula Akaunti ya Banki?",
            "tum": "Chifukwa Wuli Kujula Akaunti ya Banki?",
        },
        "body": {
            "en": "A bank account keeps your money safer than cash at home, lets you receive payments and salaries directly, and helps you build a financial history that banks look at when you apply for a loan.",
            "ny": "Akaunti ya banki imasunga ndalama zanu bwino kuposa kuzisunga kunyumba, imakuthandizani kulandira malipiro mwachindunji, ndipo imakuthandizani kupanga mbiri ya ndalama yomwe mabanki amayang'ana mukapempha ngongole.",
            "tum": "Akaunti ya banki yikusunga ndalama zinu makora kuluska kuzisunga kukaya, yikumovwira kupokelera malipiro mwendo, ndipo yikumovwira kuŵika mbiri ya ndalama iyo mabanki ghakulaŵiska para mukupempha ngongoli.",
        },
    },
    {
        "icon": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 17 9 11 13 15 21 6"/><polyline points="14 6 21 6 21 13"/></svg>''',
        "title": {
            "en": "Understanding Interest Rates",
            "ny": "Kumvetsa Chiwongola Dzanja",
            "tum": "Kupulikiska Ma-Interest",
        },
        "body": {
            "en": "A savings interest rate is what the bank pays you for keeping money with them. A loan interest rate is what you pay the bank for borrowing money. Always compare both before choosing a bank.",
            "ny": "Chiwongola dzanja cha akaunti ya sungani ndi ndalama zomwe banki imakulipirani chifukwa chosunga ndalama zanu. Chiwongola dzanja cha ngongole ndi ndalama zomwe mumalipira banki chifukwa chobwereka. Muyerekezere zonse ziwiri musanasankhe banki.",
            "tum": "Interest ya kusunga ni ndalama izo banki yikumulipilani chifukwa cha kusunga ndalama zinu. Interest ya ngongoli ni ndalama izo mukulipila banki chifukwa cha kukongola. Yaniskani vyose viŵiri pambere mundasankhe banki.",
        },
    },
    {
        "icon": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2V3z"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="9" y1="12" x2="15" y2="12"/></svg>''',
        "title": {
            "en": "Simple Budgeting",
            "ny": "Kagawidwe ka Ndalama Kosavuta",
            "tum": "Kugaŵa Ndalama Mwambura Suzgo",
        },
        "body": {
            "en": "Track what you earn and what you spend each month. A simple rule is to divide your income into needs, savings, and wants, so you always put something aside before spending.",
            "ny": "Tsatirani zomwe mumalandira ndi zomwe mumagwiritsa ntchito mwezi uliwonse. Lamulo losavuta ndikugawa ndalama zanu m'magulu atatu: zofunika, kusunga, ndi zofuna, kuti muzikhala mukusunga chinachake musanawononge.",
            "tum": "Landirani vyakuti mukupokelera na ivyo mukugwiliskira nchito mwezi uliwose. Fundo yambura suzgo ni kugaŵa ndalama zinu m'magulu ghatatu: vyakukhumbikwa, kusunga, na vyakukhumba, mwakuti muŵeko muchisunga chinthu pambere mundawononge.",
        },
    },
    {
        "icon": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 2 20h20L12 3z"/><line x1="12" y1="10" x2="12" y2="14"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>''',
        "title": {
            "en": "Avoiding Debt Traps",
            "ny": "Kupewa Misampha ya Ngongole",
            "tum": "Kuzikizga Misampha ya Ngongoli",
        },
        "body": {
            "en": "Only borrow what you can realistically repay. Before taking a loan, check the interest rate, the repayment period, and any hidden fees so the loan does not cost more than you expect.",
            "ny": "Bwerekani zomwe mungathe kubweza mosavuta. Musanatenge ngongole, onani chiwongola dzanja, nthawi yobweza, ndi ndalama zobisika kuti ngongoleyo isakuononge kuposa momwe mukuyembekezera.",
            "tum": "Kongolani waka ivyo mungawezgapo mwambura suzgo. Pambere mundapokelere ngongoli, wonani interest, nyengo ya kuwezga, na ndalama zakubisika mwakuti ngongoli yileka kumuwoneskani suzgo kuluska umo mukughanaghanira.",
        },
    },
    {
        "icon": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8" cy="12" r="2"/><line x1="14" y1="10" x2="18" y2="10"/><line x1="14" y1="14" x2="18" y2="14"/></svg>''',
        "title": {
            "en": "Why Banks Ask for KYC Documents",
            "ny": "Chifukwa Mabanki Amafuna Zikalata za KYC",
            "tum": "Chifukwa Mabanki Ghakupempha Vyoловka vya KYC",
        },
        "body": {
            "en": "\"Know Your Customer\" (KYC) checks — like your ID, proof of address, and photo — help banks confirm who you are and protect you against fraud and identity theft.",
            "ny": "Zoyezera za \"Know Your Customer\" (KYC) — monga chitupa chanu, umboni wa adilesi, ndi chithunzi — zimathandiza mabanki kutsimikizira kuti ndinu ndani ndikukutetezani ku chinyengo ndi kuba dzina.",
            "tum": "Ma-checks gha \"Know Your Customer\" (KYC) — nga umo ni chitupa chinu, ukaboni wa adilesi, na chithuzi — ghakuvwira mabanki kusimikizga umo muli, na kumuvikilirani ku uzenga na kwiba mazina.",
        },
    },
]
