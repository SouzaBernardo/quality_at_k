import json
class TextFileProcessor:  
    """
    The class handles reading, writing, and processing text files. It can read the file as JSON, read the raw text, write content to the file, and process the file by removing non-alphabetic characters.
    """

    def __init__(self, file_path):
        """
        Initialize the file path.
        :param file_path: str
        """
        self.file_path = file_path



    def read_file_as_json(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                if content.startswith('{'):
                    return json.loads(content)
                else:
                    return content
        except FileNotFoundError:
            return None

    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{"name": "test","age": 12}'
        """

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.write_file('Hello world!')
        >>> textFileProcessor.read_file()
        'Hello world!'
        """


    def process_file(self):
        content = self.read_file()
        processed_content = re.sub(r'[^a-zA-Z]', '', content)
        self.write_file(processed_content)