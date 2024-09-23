"""
adds a parent text to JSON.
"""

# Import the json module
import json

# Your text
parent_text = "National Institutes of Health (NIH) - Office of Dietary Supplements (ODS)"

# Load the JSON data from a file
with open('links.json') as f:
    data = json.load(f)

# Add the weblink as a parent to the JSON data
new_data = {parent_text: data}

# Write the new JSON data back to the original file
with open('links.json', 'w') as f:
    json.dump(new_data, f, indent=4)
