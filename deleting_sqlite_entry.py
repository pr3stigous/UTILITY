"""
identifies a specific character ending to delete from a sqlite database
"""

import sqlite3
import os

# Connect to the existing database
conn = sqlite3.connect('data2.sqlite')
cursor = conn.cursor()

# Get the table name
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_name = cursor.fetchone()[0]

# Get column names
cursor.execute(f"PRAGMA table_info({table_name})")
columns = [column[1] for column in cursor.fetchall()]

# Fetch all rows
cursor.execute(f"SELECT * FROM {table_name}")
rows = cursor.fetchall()

# Filter out rows where the URL ends with ".pdf"
filtered_rows = [row for row in rows if not row[columns.index("url")].lower().endswith('.pdf ')]

# Create a new database
new_db_name = 'data3.sqlite'
if os.path.exists(new_db_name):
    os.remove(new_db_name)

new_conn = sqlite3.connect(new_db_name)
new_cursor = new_conn.cursor()

# Create the table in the new database
column_definitions = ', '.join([f"{col} TEXT" for col in columns])
new_cursor.execute(f"CREATE TABLE {table_name} ({column_definitions})")

# Insert the filtered data into the new database
placeholders = ', '.join(['?' for _ in columns])
new_cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", filtered_rows)

# Commit changes and close connections
new_conn.commit()
new_conn.close()
conn.close()

print(f"New database '{new_db_name}' created with .pdf entries removed.")
print(f"Original entries: {len(rows)}")
print(f"Entries in new database: {len(filtered_rows)}")
