"""
fetching a website and scraping its html links - updated to included two different use cases
"""

import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage you want to get
url = "https://ods.od.nih.gov/factsheets/list-all/"

# Send HTTP request to the specified URL and save the response from server in a response object called r
r = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')

# Find both single links and categories
single_items = soup.find_all('li')
categories = soup.find_all('li', class_='category')

# Create a dictionary to store the data
data = {}

for item in single_items:
    # Extract the header/link text
    header_element = item.find('a', class_='navigation-link')

    # Check if the header element was found
    if header_element is not None:
        header = header_element.text
        # Extract and print the link
        href = header_element.get('href')
        print(f'Link: {href}')

        # Store the link
        data[header] = [href]

for category in categories:
    # Extract the header
    header_element = category.find('a', class_='handle')

    # Check if the header element was found
    if header_element is not None:
        header = header_element.text
        print(f'Header: {header}')

        # Find all links within this category
        links = category.find_all('a')

        # Create a list to store the links for this category
        data[header] = []

        for link in links:
            # Extract and print the link
            href = link.get('href')
            print(f'Link: {href}')

            # Add the link to the list for this category
            data[header].append(href)

# Save the data to a JSON file
with open('links_test5.json', 'w') as f:
    json.dump(data, f)


"""
This script will fetch the webpage content, parse it, and then print out all headers and their associated links. 
Please note that this will only work if the website does not block your IP for sending automated requests. 
If the website does block you, you might need to look into using a more sophisticated web scraping tool like Scrapy, 
which can handle things like rotating user agents and IP addresses to avoid being blocked.
"""
