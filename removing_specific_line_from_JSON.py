"""
removes specific lines from a JSON.
"""

import json

def remove_lines_from_json(json_file, lines_to_remove):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Iterate over the JSON data
    for key in data.keys():
        # If the value is a list, remove the specified lines
        if isinstance(data[key], list):
            data[key] = [item for item in data[key] if item not in lines_to_remove]

    # Write the modified data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Specify the lines to remove
lines_to_remove = ["#", "https://ods.od.nih.gov/About/exit_disclaimer.aspx"]

# Call the function
remove_lines_from_json('links.json', lines_to_remove)
