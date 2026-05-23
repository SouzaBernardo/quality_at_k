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
        try:
            data = json.load(open(file_path, 'r'))
        except FileNotFoundError:
            return -1
        else:
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
                f.write(json.dumps(data))
                return 1
        except (OSError, ValueError):
            return -1

    def process_json(self, file_path, remove_key):
        """
        read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        """
        if os.path.isfile(file_path):
            data = json.load(file_path)
            if remove_key in data:
                data = data.replace(remove_key, '')
            json.dump(data, file_path)
            return 1
        else:
            return 0