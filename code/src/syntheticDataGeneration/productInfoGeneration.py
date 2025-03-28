import pandas as pd

# Data for the CSV file
data = [
    # Bank Services
    ["Elite Privilege Banking", "An exclusive banking service for high-net-worth individuals, offering priority customer support, dedicated relationship managers, and preferential loan rates.", "Bank Services"],
    ["Infinity Savings Plus Account", "A premium savings account with unlimited free withdrawals, higher interest rates, and complimentary insurance coverage up to $100,000.", "Bank Services"],
    ["SwiftPay Instant Transfers", "A real-time money transfer service with zero transaction fees for intra-bank transfers and competitive fees for interbank transactions.", "Bank Services"],
    ["Vault Secure Locker", "A personalized safe deposit locker service available in small, medium, and large sizes, with biometric access for added security.", "Bank Services"],
    ["Platinum Business Current Account", "A current account designed for SMEs and startups, featuring zero balance requirements, free bulk payments, and cash deposit limits of up to $1 million/month.", "Bank Services"],
    ["Flexi Fixed Deposit", "A unique FD that allows partial withdrawals without breaking the entire deposit while still earning interest on the remaining balance.", "Bank Services"],
    ["Signature Cheque Protection", "A service ensuring all cheques issued from the account are verified via a two-factor authentication process before clearance.", "Bank Services"],
    ["Wealth Premier Relationship Plan", "A bundled banking package offering free investment advisory, annual financial health checks, and exclusive networking events.", "Bank Services"],
    ["Prime Foreign Currency Account", "A multi-currency account allowing customers to hold and transact in USD, EUR, GBP, and JPY with zero conversion charges on international purchases.", "Bank Services"],
    ["AutoPay Smart Billing", "A feature enabling automatic bill payments for utilities, credit cards, and subscriptions with real-time transaction tracking via the bank’s mobile app.", "Bank Services"],

    # Investment Services
    ["GoldMax Wealth Fund", "A high-yield mutual fund focusing on investments in gold-backed securities, offering liquidity and stable returns with a minimum investment of $10,000.", "Investment Services"],
    ["NextGen Tech Fund", "A sector-specific mutual fund investing in AI, blockchain, and clean energy startups, aimed at aggressive investors seeking long-term capital appreciation.", "Investment Services"],
    ["Infinity Retirement Plus Plan", "A personalized pension scheme offering tax benefits and flexible payout options, designed for professionals and business owners planning post-retirement income.", "Investment Services"],
    ["Dynamic Equity-Linked Savings Plan", "A tax-saving investment that allocates funds between high-growth equity and stable debt instruments, rebalancing quarterly based on market conditions.", "Investment Services"],
    ["Titan Blue Chip Stock Basket", "A curated portfolio of top-performing blue-chip stocks managed by the bank’s investment research team, with quarterly reallocation for optimal growth.", "Investment Services"],
    ["Secure Wealth Bond Series", "A fixed-income investment with a tenure of 5–10 years, offering guaranteed returns and insurance-backed security for capital protection.", "Investment Services"],
    ["Millennial SIP Booster", "A systematic investment plan (SIP) that auto-adjusts investment amounts based on monthly spending patterns, ensuring optimal savings without financial strain.", "Investment Services"],
    ["Green Future Infrastructure REIT", "A real estate investment trust (REIT) focused on sustainable infrastructure projects, offering dividend-based passive income.", "Investment Services"],
    ["Infinity Capital Smart ULIP", "A market-linked insurance plan that dynamically switches between equity and debt funds based on investor risk profiles.", "Investment Services"],
    ["Startup Angel Investment Gateway", "A unique investment platform connecting accredited investors with vetted startups, allowing fractional equity investments with exit options after 3 years.", "Investment Services"],

    # Other Services
    ["Credit Score Accelerator Program", "A financial wellness tool that helps customers improve their credit score by analyzing spending habits and suggesting optimal repayment strategies.", "Other Services"],
    ["SafePay Fraud Protection Suite", "A cybersecurity service providing AI-driven transaction monitoring, instant fraud alerts, and zero-liability protection against unauthorized banking activity.", "Other Services"],
    ["TaxSmart Pro Advisory", "A digital tax advisory service offering automated income tax calculations, investment-linked deductions, and expert consultations for compliance optimization.", "Other Services"],
    ["Infinity Expense Tracker AI", "An AI-powered budgeting tool that categorizes expenses, provides saving recommendations, and automates bill payments for financial discipline.", "Other Services"],
    ["CryptoLink Investment Portal", "A secure cryptocurrency trading platform with instant conversion to fiat currency and blockchain-backed transaction verification.", "Other Services"],
    ["Legal Trust & Will Planning Suite", "A guided estate planning tool that enables users to create legally binding wills, assign power of attorney, and manage inheritance documentation digitally.", "Other Services"],
    ["Global Remit Express", "An international money transfer service with real-time exchange rate tracking and low-cost transfers to 50+ countries.", "Other Services"],
    ["Virtual Card Vault", "A digital platform allowing customers to generate temporary, one-time-use virtual cards for online transactions, reducing the risk of fraud.", "Other Services"],
    ["SafeHome Insurance Planner", "A policy recommendation tool that compares home insurance plans based on property type, location, and risk factors to suggest the best coverage.", "Other Services"],
    ["Personalized Loan Pre-Approval Checker", "A predictive tool that estimates loan eligibility and interest rates based on real-time credit analysis, reducing the need for manual approval processes.", "Other Services"],
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["Product Name", "Description", "Category"])

# Save as CSV
file_path = "../data/ProductsData/synthetic_bank_services_dataset.csv"
df.to_csv(file_path, index=False)

