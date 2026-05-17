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
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(e)
            return str(e)


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
        with open(self.file_path, 'r') as f:
            content = f.read()
            content = content.replace('"', '').replace('\'', '')
            content = content.replace(' ', '')
            content = content.replace('\n', '')
            content = content.replace('\t', '')
            content = content.replace('\r', '')
            content = content.replace('\b', '')
            content = content.replace('\f', '')
            content = content.replace('\v', '')
            content = content.replace('\0', '')
            content = content.replace('\x1b', '')
            content = content.replace('\x1c', '')
            content = content.replace('\x1d', '')
            content = content.replace('\x1e', '')
            content = content.replace('\x1f', '')
            content = content.replace('\x7f', '')
            content = content.replace('\x80', '')
            content = content.replace('\x81', '')
            content = content.replace('\x82', '')
            content = content.replace('\x83', '')
            content = content.replace('\x84', '')
            content = content.replace('\x85', '')
            content = content.replace('\x86', '')
            content = content.replace('\x87', '')
            content = content.replace('\x88', '')
            content = content.replace('\x89', '')
            content = content.replace('\x8a', '')
            content = content.replace('\x8b', '')
            content = content.replace('\x8c', '')
            content = content.replace('\x8d', '')
            content = content.replace('\x8e', '')
            content = content.replace('\x8f', '')
            content = content.replace('\x90', '')
            content = content.replace('\x91', '')
            content = content.replace('\x92', '')
            content = content.replace('\x93', '')
            content = content.replace('\x94', '')
            content = content.replace('\x95', '')
            content = content.replace('\x96', '')
            content = content.replace('\x97', '')
            content = content.replace('\x98', '')
            content = content.replace('\x99', '')
            content = content.replace('\x9a', '')
            content = content.replace('\x9b', '')
            content = content.replace('\x9c', '')
            content = content.replace('\x9d', '')
            content = content.replace('\x9e', '')
            content = content.replace('\x9f', '')
            content = content.replace('\xa0', '')
            content = content.replace('\xa1', '')
            content = content.replace('\xa2', '')
            content = content.replace('\xa3', '')
            content = content.replace('\xa4', '')
            content = content.replace('\xa5', '')
            content = content.replace('\xa6', '')
            content = content.replace('\xa7', '')
            content = content.replace('\xa8', '')
            content = content.replace('\xa9', '')
            content = content.replace('\xaa', '')
            content = content.replace('\xab', '')
            content = content.replace('\xac', '')
            content = content.replace('\xad', '')
            content = content.replace('\xae', '')
            content = content.replace('\xaf', '')
            content = content.replace('\xb0', '')
            content = content.replace('\xb1', '')
            content = content.replace('\xb2', '')
            content = content.replace('\xb3', '')
            content = content.replace('\xb4', '')
            content = content.replace('\xb5', '')
            content = content.replace('\xb6', '')
            content = content.replace('\xb7', '')
            content = content.replace('\xb8', '')
            content = content.replace('\xb