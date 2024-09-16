import sqlite3

def create_connection():
    """Create a database connection to a SQLite database."""
    try:
        conn = sqlite3.connect('example.db')
        print("Connection to SQLite database successful.")
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

def close_connection(conn):
    """Close the database connection."""
    if conn:
        conn.close()
        print("Connection closed.")

def create_table(conn):
    """Create a sample table if it doesn't exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        print("Table 'users' created successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def insert_user(conn, username, email):
    """Insert a user into the 'users' table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email) VALUES (?, ?)
        ''', (username, email))
        conn.commit()
        print(f"User '{username}' inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def select_all_users(conn):
    """Select all users from the 'users' table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users
        ''')
        rows = cursor.fetchall()
        print("All users:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error: {e}")

# Example usage
connection = create_connection()

if connection:
    create_table(connection)
    insert_user(connection, 'john_doe', 'john@example.com')
    insert_user(connection, 'jane_doe', 'jane@example.com')
    select_all_users(connection)

    close_connection(connection)

