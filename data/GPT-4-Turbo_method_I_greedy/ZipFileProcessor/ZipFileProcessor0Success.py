import zipfile
class ZipFileProcessor: 
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
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            zip_file = self.read_zip_file()
            if zip_file is not None:
                zip_file.extractall(output_path)
                zip_file.close()
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            zip_file = self.read_zip_file()
            if zip_file is not None:
                zip_file.extract(file_name, output_path)
                zip_file.close()
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zipf:
                for file in files:
                    zipf.write(file)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False