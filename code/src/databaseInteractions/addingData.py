import pandas as pd
from crud_operations_helper import insert_record
import csv

# # Adding Dummy Data for customerAccountData
# csv_filename1 = "../data/customerAccountDummyData.csv"
# try:
#     df = pd.read_csv(csv_filename1)
# except FileNotFoundError:
#     print(f"Error: File '{csv_filename1}' not found.")
#     exit()

# for _, row in df.iterrows():
#     record = {
#         "customerID": row["customerID"],
#         "accountNumber": row["accountNumber"],
#         "accountBalance": row["accountBalance"],
#         "creditCardAvailable": row["creditCardAvailable"], 
#         "creditLimit": row["creditLimit"],
#         "percentageUsed": row["percentageUsed"]
#     }
#     insert_record("customerAccountData", record)


# Adding Actual Data for previousTransactions
csv_filename2 = "../data/previousTransactionHistory.csv"
with open(csv_filename2, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Read CSV into dictionaries

    for row in reader:
        try:
            # Transform column names to match database schema
            record = {
                "CustomerID": row["CustomerID"],
                "CustGender": row["CustGender"],
                "CustAccountBalance": float(row["CustAccountBalance"]),
                "TransactionDate": row["TransactionDate"].strip(),
                "TransactionTime": row["TransactionTime"].strip(),
                "TransactionAmount": float(row["TransactionAmount (INR)"])  # Rename key to match DB
            }

            # Insert the row using the provided insert_record function
            insert_record("previousTransactions", record)

        except Exception as e:
            print(f"Skipping row due to error: {e}")


print("All records inserted successfully into customerAccountData.")
