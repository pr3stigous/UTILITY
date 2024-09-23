"""
removes lines from a JSON that include a specific text. 
"""

import json

def remove_lines_from_json(json_file, texts_to_remove):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Iterate over the JSON data
    for key in data.keys():
        # If the value is a list, remove the lines that include the specified texts
        if isinstance(data[key], list):
            for text in texts_to_remove:
                data[key] = [item for item in data[key] if text not in item]

    # Write the modified data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Specify the texts to remove lines for
texts_to_remove = ["#", "/About/exit"]

# Call the function
remove_lines_from_json('links_ref2.json', texts_to_remove)
