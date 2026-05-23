import json
import os
class JSONProcessor: 


    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :param file_path: str, the path of the JSON file.
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        """
        if not os.path.exists(file_path):
            return 0
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return -1

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
            return 1
        except Exception as e:
            print(f"Error writing JSON file: {e}")
            return -1

    def process_json(self, file_path, remove_key):
        """
        Read a JSON file, process the data by removing a specified key, and write the modified data back to the file.
        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                   0, if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)
        if data is None:
            return 0
        if remove_key not in data:
            return 0
        del data[remove_key]
        self.write_json(data, file_path)
        return 1