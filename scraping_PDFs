"""
used to scrape PDFs from a website
"""

import os
from requests_html import HTMLSession
from pathlib import Path
from PyPDF2 import PdfFileReader
import hashlib

# Step 1: Specify the URL of the website to scrape
website_url = 'www.urlhere.com'  # Replace with the target URL

# Create a directory to save PDFs
output_dir = Path("downloaded_pdfs")
output_dir.mkdir(exist_ok=True)

# Step 2: Scrape the website to find all PDF links
def get_pdf_links(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1)  # Wait for JavaScript to execute

    # Collect all possible links to PDFs
    pdf_links = [a.absolute_links.pop() for a in response.html.find('div.download-module a') if a.absolute_links]

    return pdf_links

# Step 3: Download PDFs
def download_pdf(pdf_url):
    # Extract the PDF name from the URL
    pdf_name = pdf_url.split("/")[-1]

    # If the PDF name is empty, generate a name from the URL
    if not pdf_name:
        pdf_name = 'file_' + hashlib.md5(pdf_url.encode()).hexdigest() + '.pdf'

    pdf_path = output_dir / pdf_name

    print(f"Downloading {pdf_name}...")
    try:
        # Download the PDF
        session = HTMLSession()
        response = session.get(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print(f"Saved {pdf_name} to {pdf_path}")
    except Exception as e:
        print(f"Failed to download {pdf_url}, Error: {str(e)}")

# Step 4: Execute the script
if __name__ == "__main__":
    # Get all PDF links from the website
    pdf_links = get_pdf_links(website_url)
    print(f"Found {len(pdf_links)} PDF links.")

    # Download each PDF
    for pdf_link in pdf_links:
        download_pdf(pdf_link)
