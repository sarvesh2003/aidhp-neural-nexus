import csv
import os
from datetime import datetime
from flask import request, jsonify
from config import app

# ------------------------------------------------------------------------------------------
# TRANSACTIONS ENDPOINTS
# ------------------------------------------------------------------------------------------

CREDIT_CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'creditCardTransactions.csv')
DEBIT_CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'previousTransactionHistory.csv')

def get_latest_transaction(user_id):
    try:
        with open(DEBIT_CSV_FILE_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            transactions = [row for row in reader if row['CustomerID'] == user_id]
            if transactions:
                return transactions[-1]
    except FileNotFoundError:
        return None
    return None

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    current_datetime = datetime.now()
    credit_timestamp = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    debit_date = current_datetime.strftime('%d/%m/%y')
    debit_time = current_datetime.strftime('%H%M%S')

    if data['transactionType'] == 'credit':
        try:
            required_fields = ['user', 'card', 'amount', 'useChip', 'merchantName', 'merchantCity', 'merchantState', 'zip']
            for field in required_fields:
                if field not in data or not data[field]:
                    return jsonify({'error': f'Missing or invalid field: {field}'}), 400

            with open(CREDIT_CSV_FILE_PATH, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([
                    data['user'],
                    data['card'],
                    data['amount'],
                    data['useChip'],
                    data['merchantName'],
                    data['merchantCity'],
                    data['merchantState'],
                    data['zip'],
                    credit_timestamp
                ])
            return jsonify({'message': 'Credit card transaction added successfully'}), 201
        except Exception as e:
            print(f"Error processing credit transaction: {e}")
            return jsonify({'error': 'An error occurred while processing the credit transaction'}), 500

    elif data['transactionType'] == 'debit':
        try:
            user_id = data.get('customerID')
            amount = float(data.get('transactionAmount', 0))

            if not user_id or amount <= 0:
                return jsonify({'error': 'Invalid CustomerID or transaction amount'}), 400

            latest_transaction = get_latest_transaction(user_id)

            if not latest_transaction:
                return jsonify({'error': 'Invalid CustomerID'}), 400

            gender = latest_transaction['CustGender']
            balance = float(latest_transaction['CustAccountBalance'])

            if balance < amount:
                return jsonify({'error': 'Insufficient balance'}), 400

            new_balance = balance - amount

            with open(DEBIT_CSV_FILE_PATH, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([
                    user_id,
                    gender,
                    f"{new_balance:.2f}",
                    debit_date,
                    debit_time,
                    f"{amount:.2f}"
                ])
            return jsonify({'message': 'Debit card transaction added successfully'}), 201
        except Exception as e:
            print(f"Error processing debit transaction: {e}")
            return jsonify({'error': 'An error occurred while processing the debit transaction'}), 500

    else:
        return jsonify({'error': 'Invalid transaction type'}), 400

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transaction_type = request.args.get('type')
    user_id = request.args.get('user')
    transactions = []
    if transaction_type == 'credit':
        with open(CREDIT_CSV_FILE_PATH, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == user_id:
                    transactions.append({
                        'user': row[0],
                        'card': row[1],
                        'amount': row[2],
                        'useChip': row[3],
                        'merchantName': row[4],
                        'merchantCity': row[5],
                        'merchantState': row[6],
                        'zip': row[7],
                        'timestamp': row[8]
                    })
    elif transaction_type == 'debit':
        with open(DEBIT_CSV_FILE_PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['CustomerID'] == user_id:
                    transactions.append({
                        'CustomerID': row['CustomerID'],
                        'TransactionAmount': row['TransactionAmount (INR)'],
                        'TransactionDate': row['TransactionDate'],
                        'TransactionTime': row['TransactionTime']
                    })

    if not transactions:
        return jsonify({'message': 'No records found'}), 404
    return jsonify(transactions)

# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
# RECOMMENDATION ENDPOINTS
# ------------------------------------------------------------------------------------------

BANK_LOANS_CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'ProductsData', 'bank_loans.csv')

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    recommendations = []
    print(f"Reading recommendations from {BANK_LOANS_CSV_FILE_PATH}")
    try:
        with open(BANK_LOANS_CSV_FILE_PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recommendations.append({
                    'product': row['Product Name'],
                    'description': row['Description']
                })
        return jsonify(recommendations), 200
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        print(f"Error reading recommendations: {e}")
        return jsonify({'error': 'An error occurred while fetching recommendations'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)