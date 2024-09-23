"""
adds self-defined data to lines within a JSON.
"""

import json

# Load your JSON data from a file
with open('links.json', 'r') as f:
    data = json.load(f)

# Iterate over the data
for key in data:
    for i, link in enumerate(data[key]):
        # Check if the link starts with "/factsheet"
        if link.startswith("/"):
            # Add "https://ods.od.nih.gov" in front of the link
            data[key][i] = "https://ods.od.nih.gov" + link

# Save the updated data back to the file
with open('links.json', 'w') as f:
    json.dump(data, f, indent=4)
