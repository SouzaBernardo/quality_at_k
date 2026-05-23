import json
import os
class JSONProcessor: 

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :param file_path: str, the path of the JSON file.
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
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

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)
        if data and remove_key in data:
            del data[remove_key]
            self.write_json(data, file_path)
            return 1
        else:
            return 0

