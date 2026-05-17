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
        if not os.path.exists(self.file_path):
            raise FileNotFoundError('File not found: {}'.format(self.file_path))
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data


    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{\n    "name": "test",\n    "age": 12\n}'
        """
        with open(self.file_path, 'r') as f:
            content = f.read()
        return content


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
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{\n    "name": "test",\n    "age": 12\n}'
        >>> textFileProcessor.process_file()
        'nametestage'
        """
        self.file_path = open(self.file_path, 'r')
        content = self.file_path.read()
        self.file_path.close()
        content = content.replace('\n', '')
        content = content.replace('"', '')
        content = content.replace(' ', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
        content = content.replace('"', '')
     