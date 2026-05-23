import json
class TextFileProcessor: 
    def __init__(self, file_path):
        """
        Initialize the file path.
        :param file_path: str
        """
        self.file_path = file_path





    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{\n    "name": "test",\n    "age": 12\n}'
        """
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('Hello world!')
        >>> textFileProcessor.read_file()
        'Hello world!'
        """
        with open(self.file_path, 'w') as f:
            f.write(content)

    def process_file(self):
        """
        Process the self.file_path file by removing non-alphabetic characters.
        :return: processed_data
        """
        with open(self.file_path, 'r') as file:
            file_data = file.read()
        processed_data = ''.join(c for c in file_data if c.isalpha())
        return processed_data