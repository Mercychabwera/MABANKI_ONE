u"""Static content used by the app: participating banks and financial
literacy tips, each provided in English, Chichewa and Chitumbuka."""

BANKS = [
    {
        "name": "National Bank of Malawi",
        "logo": "img/bank-logos/nbm.svg",
        "savings": "10% per year",
        "loan": "24% per year",
        "opening": "MK5,000",
    },
    {
        "name": "Standard Bank Malawi",
        "logo": "img/bank-logos/standard.ico",
        "savings": "9% per year",
        "loan": "22% per year",
        "opening": "MK10,000",
    },
    {
        "name": "FDH Bank",
        "logo": "img/bank-logos/fdh.png",
        "savings": "8% per year",
        "loan": "20% per year",
        "opening": "MK2,000",
    },
    {
        "name": "NBS Bank",
        "logo": "img/bank-logos/nbs.png",
        "savings": "9.5% per year",
        "loan": "23% per year",
        "opening": "MK5,000",
    },
    {
        "name": "CDH Bank",
        "logo": "img/bank-logos/cdh.svg",
        "savings": "8.5% per year",
        "loan": "21% per year",
        "opening": "MK3,000",
    },
    {
        "name": "Ecobank Malawi",
        "logo": "img/bank-logos/ecobank.svg",
        "savings": "9% per year",
        "loan": "22.5% per year",
        "opening": "MK5,000",
    },
]

LITERACY_TIPS = [
    {
        "icon": "🏦",
        "title": {
            "en": "Why do you want to Open a Bank Account?",
            "ny": "Bwanji mwafuna kutsegula Akaunti ya Banki?",
            "tum": "Chifukwa Wuli Kujula Akaunti ya Banki?",
        },
        "body": {
            "en": "A bank account keeps your money safer than cash at home, lets you receive payments and salaries directly and helps you build a financial history that banks look at when you apply for a loan.",
            "ny": "Akaunti ya banki imasunga ndalama zanu bwino kuposa kuzisunga kunyumba, imakuthandizani kulandira malipiro mwachindunji ndipo imakuthandizani kupanga mbiri ya ndalama yomwe mabanki amayang'ana mukapempha ngongole.",
            "tum": "Akaunti ya banki yikusunga ndalama zinu makora kuluska kuzisunga kukaya, yikumovwira kupokelera malipiro mwendo, ndipo yikumovwira kuŵika mbiri ya ndalama iyo mabanki ghakulaŵiska para mukupempha ngongoli.",
        },
    },
    {
        "icon": "📈",
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
        "icon": "🧾",
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
        "icon": "⚠️",
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
        "icon": "📄",
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
