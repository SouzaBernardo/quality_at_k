import json
class TextFileProcessor: 
    def __init__(self, file_path):
        """
        Initialize the file path.
        :param file_path: str
        """
        self.file_path = file_path



    def read_file_as_json(self):
        """
        Read the self.file_path file as json format.
        if the file content doesn't obey json format, the code will raise error.
        :return data: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file_as_json()
        {'name': 'test', 'age': 12}
        >>> type(textFileProcessor.read_file_as_json())
        <class 'dict'>
        """
        with open(self.file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = file.read()
        return data


    def read_file(self):
        """
        Read and return the content of self.file_path file.
        :return: the same return as the read() method
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
        return content
    

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        """
        with open(self.file_path, 'w') as file:
            file.write(content)
    

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
    
        processed_content = ''.join(c for c in content if c.isalpha())
    
        with open(self.file_path, 'w') as file:
            file.write(processed_content)
    
        return processed_content