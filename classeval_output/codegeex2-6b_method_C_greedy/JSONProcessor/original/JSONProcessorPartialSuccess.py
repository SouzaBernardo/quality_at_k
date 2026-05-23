import json
import os
class JSONProcessor: 


    def read_json(self, file_path):
        

        if not os.path.exists(file_path):
            return 0

        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                return -1

        return data


    def write_json(self, data, file_path):
        

        with open(file_path, 'w') as f:
            json.dump(data, f)

        return 1



    def remove_key(self, data, key):


    def process_json(self, file_path, remove_key):
