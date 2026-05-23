import json
import os
class JSONProcessor: 


    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return -1

    def write_json(self, data, file_path):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            return 1
        except Exception as e:
            return -1

    def process_json(self, file_path, remove_key):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            if remove_key in data:
                data.pop(remove_key)
            with open(file_path, 'w') as f:
                json.dump(data, f)
            return 1
        except (FileNotFoundError, ValueError) as e:
            return 0