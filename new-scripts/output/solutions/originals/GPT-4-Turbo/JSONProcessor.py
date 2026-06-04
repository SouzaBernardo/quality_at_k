```python
import json
import os

class JSONProcessor:
    """
    This is a class to process JSON file, including reading and writing JSON files, as well as processing JSON data by removing a specified key from the JSON object.
    """

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        """
        if not os.path.exists(file_path):
            return 0
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return -1

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file)
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return -1

    def process_json(self, file_path, remove_key):
        """
        read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.
        """
        data = self.read_json(file_path)
        if data == 0 or data == -1:
            return 0
        if remove_key in data:
            del data[remove_key]
            self.write_json(data, file_path)
            return 1
        else:
            return 0
```