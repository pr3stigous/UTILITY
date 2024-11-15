"""
extracts html from a weblink and saved into a sqlite database
it also hashes said html using MD5 which can be used as a uniqueID that does not require its own naming convention = easily scalable
"""

import hashlib
import requests
from bs4 import BeautifulSoup
import json
import sqlite3

# Function to generate MD5 hash for a given url
def generate_hash(url):
    return hashlib.md5(url.encode('utf-8')).hexdigest()

# Connect sqlite
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()

# Create table if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS webdata
             (hash TEXT, url TEXT, html TEXT)''')

with open("new_links.json") as f:
    data = json.load(f)

    # Create a Session
    session = requests.Session()

    for link in data['links']:
        try:
            res = session.get(link)
            soup = BeautifulSoup(res.text, 'html.parser')
            html = str(soup)

            hash_ = generate_hash(link)
            cursor.execute("INSERT INTO webdata VALUES (?, ?, ?)",
                        (hash_, link, html))

        except requests.exceptions.ConnectionError as e:
            print(f"Failed to connect to {link}. The error was {str(e)}.")

conn.commit()
conn.close()



"""
Before running the script, you need to install the necessary Python packages with pip:

pip install requests beautifulsoup4

"""
