import sqlite3

def initialize_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("../database/hackathon-db.sqlite")
    cursor = conn.cursor()

    # Create UserTransactionsInsights table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserTransactionsInsights (
            Username TEXT PRIMARY KEY,
            AverageTransactionAmount REAL,
            AverageCardTransactionAmount REAL,
            RecommendationRelevanceRatio REAL
        )
    ''')

    # Create SocialMediaInteractionInfo table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SocialMediaInteractionInfo (
            Username TEXT PRIMARY KEY,
            LastInteraction DATE
        )
    ''')

    # Create customerAccountData table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customerAccountData (
            customerID TEXT PRIMARY KEY,
            accountNumber TEXT UNIQUE,
            accountBalance REAL,
            creditCardAvailable INTEGER DEFAULT 0,
            creditLimit REAL,
            percentageUsed REAL
        )
    """)

    # Create the previousTransactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS previousTransactions (
            CustomerID TEXT,
            CustGender TEXT,
            CustAccountBalance REAL,
            TransactionDate TEXT,
            TransactionTime TEXT,
            TransactionAmount REAL
        )
    ''')

    

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database and tables initialized successfully.")
