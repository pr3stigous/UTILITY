"""
code used to reduce a sqlite database so i can use as a test file
"""

import sqlite3
import os

# Input and output file names
input_db = 'data2.sqlite'
output_db = 'data2_sample.sqlite'

# Ensure the input database exists
if not os.path.exists(input_db):
    print(f"Error: Input database '{input_db}' not found.")
    exit(1)

# Connect to the input database
conn_input = sqlite3.connect(input_db)
cursor_input = conn_input.cursor()

# Create a new output database
conn_output = sqlite3.connect(output_db)
cursor_output = conn_output.cursor()

# Get the list of tables in the input database
cursor_input.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor_input.fetchall()

for table in tables:
    table_name = table[0]
    
    # Get the table schema
    cursor_input.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    schema = cursor_input.fetchone()[0]
    
    # Create the table in the output database
    cursor_output.execute(schema)
    
    # Copy random 20 rows from the input to the output
    cursor_input.execute(f"SELECT * FROM {table_name} ORDER BY RANDOM() LIMIT 20;")
    rows = cursor_input.fetchall()
    
    # Get column names
    cursor_input.execute(f"PRAGMA table_info({table_name});")
    columns = [column[1] for column in cursor_input.fetchall()]
    placeholders = ','.join(['?' for _ in columns])
    
    # Insert the rows into the output database
    cursor_output.executemany(f"INSERT INTO {table_name} VALUES ({placeholders});", rows)

# Commit changes and close connections
conn_output.commit()
conn_input.close()
conn_output.close()

print(f"New database with 20 entries per table has been created: {output_db}")
