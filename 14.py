import sqlite3
import csv

# Database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Read data from CSV file
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
            INSERT INTO users (id, name, email)
            VALUES (:id, :name, :email)
        ''', row)

# Commit and close
conn.commit()
conn.close()
