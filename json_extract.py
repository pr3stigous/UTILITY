"""
used to extract from one json to another with formatting 
that fits better for a different task
"""

import json

# Read the original JSON file
with open('links.json', 'r') as file:
    data = json.load(file)

# Extract all links
links = []
for category in data.values():
    for subcategory in category.values():
        for item in subcategory.values():
            if isinstance(item, list):
                links.extend(item)

# Create the new JSON structure
output = {
    "links": links
}

# Write the new JSON file
with open('new_links.json', 'w') as file:
    json.dump(output, file, indent=4)

print(f"Extracted {len(links)} links and saved to output.json")
