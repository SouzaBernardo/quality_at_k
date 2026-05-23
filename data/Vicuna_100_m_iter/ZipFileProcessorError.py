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
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                return zip_file.open()
        except zipfile.BadZipfile as e:
            print(f"Error: {e}")
            return None

    def extract_all(self, output_path):
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                for zip_file_path, dir_list, file_list in zip_file.infolist():
                    if not zip_file_path.endswith(self.file_name):
                        dir_list.pop(0)
                        file_list.pop(0)
                    for dir_path, dir_list, file_list in zip_file.infolist():
                        if not dir_path.startswith(self.file_name):
                            dir_list.pop(0)
                            file_list.pop(0)
                    for file_path, file_list in zip_file.infolist():
                        if not file_path.endswith(self.file_name):
                            file_list.pop(0)
                        with zipfile.ZipFile(file_path, 'r') as sub_zip_file:
                            sub_zip_file.extractall(output_path)
            return True
        except zipfile.BadZipfile as e:
            print(f"Error: {e}")
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extract(file_name, output_path)
                return True
        except zipfile.BadZipfile as e:
            print(f"Error: {e}")
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return: True or False, representing whether the compression operation was successful
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file_name in files:
                    zip_file.write(file_name)
                return True
        except zipfile.BadZipfile as e:
            print(f"Error: {e}")
            return False