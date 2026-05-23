import json
import os
class JSONProcessor:  
    """
    This is a class to process JSON file, including reading and writing JSON files, as well as processing JSON data by removing a specified key from the JSON object.
    """



    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            return {'error': 'File does not exist'}
        except json.JSONDecodeError as e:
            return {'error': 'Invalid JSON format'}
        return data

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.

        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: 1 if the writing process is successful, or -1, if an error occurs during the writing process.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f)
        except FileNotFoundError:
            return {'error': 'File does not exist'}
        except json.JSONDecodeError as e:
            return {'error': 'Invalid JSON format'}
        return 1

    def process_json(self, file_path, remove_key):
        """
        read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            if remove_key in data:
                data = data.replace(remove_key, '')
            if len(data) == 0:
                return 0
            return 1
        except FileNotFoundError:
            return {'error': 'File does not exist'}
        except json.JSONDecodeError as e:
            return {'error': 'Invalid JSON format'}