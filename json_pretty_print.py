"""
making JSON output look pretty.
"""

import json

# Load the data from the JSON file
with open('links_ref.json') as f:
    data = json.load(f)

# Write the data back to the file, pretty-printed
with open('links_ref.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
