import csv
import sqlite3
import os
import re

# --- Configuration (DO NOT hardcode secrets) ---
DB_PATH = os.getenv("DB_PATH", "example.db")  # Use environment variable or fallback

# --- Input validation function ---
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# --- Connect to SQLite database ---
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# --- Create table if it doesn't exist ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# --- Read from CSV and insert data ---
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # Validate and sanitize input
            user_id = int(row['id'])
            name = row['name'].strip()
            email = row['email'].strip()
            
            if not is_valid_email(email):
                raise ValueError(f"Invalid email: {email}")

            # Insert using parameterized query (avoids SQL injection)
            cursor.execute('''
                INSERT INTO users (id, name, email)
                VALUES (?, ?, ?)
            ''', (user_id, name, email))
        
        except Exception as e:
            print(f"Skipping row due to error: {e}")

# --- Commit and close ---
conn.commit()
conn.close()
