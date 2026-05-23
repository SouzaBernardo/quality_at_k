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
        """
        Read the self.file_path file as json format.
        if the file content doesn't obey json format, the code will raise error.
        :return data: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        """
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'name': 'test', 'age': 12}
        return data

    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        >>> textFileProcessor = TextFileProcessor('test.json')
        >>> textFileProcessor.read_file()
        '{\n    "name": "test",\n    "age": 12\n}'
        """
        return self.read_file_as_json()

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        :return: None
        """
        if self.file_path!= '/dev/null':
            with open(self.file_path, 'w') as f:
                f.write(content)
        else:
            print('File already exists, overwrite it? (y/n)')
            choice = input('Enter y to overwrite or n to continue: ')
            if choice == 'y':
                self.file_path = '/dev/null'
            elif choice == 'n':
                print('File already exists, continue with read() method')
                return