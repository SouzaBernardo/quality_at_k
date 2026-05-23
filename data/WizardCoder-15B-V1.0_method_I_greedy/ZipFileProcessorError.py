import zipfile
class ZipFileProcessor:  
    """
    This is a compressed file processing class that provides the ability to read and decompress compressed files
    """

    def __init__(self, file_name):
        """
        Initialize file name
        :param file_name:string
        """
        self.file_name = file_name



    def read_zip_file(self):
        """
        Get open file object
        :return:If successful, returns the open file object; otherwise, returns None
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                file_names = zip_ref.namelist()
                for file_name in file_names:
                    with zip_ref.open(file_name, 'r') as file:
                        content = file.read()
                        print(content)
            return file
        except zipfile.BadZipFile:
            print("Invalid zip file")
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        except zipfile.BadZipFile:
            print("Invalid zip file")
            return False



    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_ref:
                for file in files:
                    zip_ref.write(file)
            return True
        except:
            return False