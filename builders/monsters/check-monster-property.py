import os
import json
import config
from pathlib import Path

def read_json_files():
    property_name = "attack_type"
    folder_path = Path(config.DOCS_PATH, "monsters-json")
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    files_with_empty_property = []  # List to store file names with empty property

    for file_name in files:
        # Check if the file is a JSON file
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                try:
                    # Load the JSON data
                    data = json.load(file)

                    # Check if the property exists in the JSON object
                    if property_name in data:
                        property_value = data[property_name]
                        # Check if the property value is an empty list
                        if isinstance(property_value, list) and len(property_value) == 0:
                            files_with_empty_property.append(file_name)
                    else:
                        print(f"Property '{property_name}' not found in '{file_name}'")
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON in '{file_name}': {str(e)}")

    if files_with_empty_property:
        print(f"Missing count: '{len(files_with_empty_property)}'")
        print(f"Missing list: '{files_with_empty_property}'")
        # print("Files with empty property value:")
        # for file_name in files_with_empty_property:
        #     print(file_name)
    else:
        print("No files found with empty property value.")

if __name__ == '__main__':
    read_json_files()
