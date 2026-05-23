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
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except:
            return -1
    

    def write_json(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            return 1
        except Exception as e:
            print(f"Error writing JSON file: {e}")
            return -1


    def process_json(self, file_path, remove_key):
        """
        Read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.
    
        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                 0, if the file does not exist or the specified key does not exist in the data.
        """
        # Check if the file exists
        if not os.path.exists(file_path):
            return 0
    
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
    
        # Check if the specified key exists in the data
        if remove_key not in data:
            return 0
    
        # Remove the specified key from the data
        del data[remove_key]
    
        # Write the modified data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file)
    
        return 1