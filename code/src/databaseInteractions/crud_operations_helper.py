import sqlite3

def insert_record(table_name, data):

    conn = sqlite3.connect("../database/hackathon-db.sqlite")
    cursor = conn.cursor()

    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    try:
        cursor.execute(query, tuple(data.values()))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting record:", e)
    finally:
        conn.close()

def read_records(table_name):

    conn = sqlite3.connect("hackathon-db.sqlite")
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print("Error reading records:", e)
        return []
    finally:
        conn.close()

def update_record(table_name, identifier_column, identifier_value, updated_data):

    conn = sqlite3.connect("hackathon-db.sqlite")
    cursor = conn.cursor()

    set_clause = ', '.join([f"{col} = ?" for col in updated_data.keys()])
    query = f"UPDATE {table_name} SET {set_clause} WHERE {identifier_column} = ?"

    try:
        cursor.execute(query, tuple(updated_data.values()) + (identifier_value,))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print("Error updating record:", e)
    finally:
        conn.close()

def delete_record(table_name, identifier_column, identifier_value):
    """
    Delete a record from the specified table.
    :param table_name: Name of the table
    :param identifier_column: Primary key column name
    :param identifier_value: Value of the primary key to find the record
    """
    conn = sqlite3.connect("hackathon-db.sqlite")
    cursor = conn.cursor()

    query = f"DELETE FROM {table_name} WHERE {identifier_column} = ?"
    
    try:
        cursor.execute(query, (identifier_value,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting record:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    print("Contents: ", read_records("UserTransactionsInsights"))
    print("CRUD functions module. Import and use the functions as needed.")
