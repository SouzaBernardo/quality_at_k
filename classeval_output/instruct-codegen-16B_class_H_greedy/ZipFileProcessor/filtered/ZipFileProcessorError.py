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
            zf = zipfile.ZipFile(self.file_name)
            return zf
            # If the file is not a zip file, return None
            except zipfile.BadZipfile:
                return None
    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            zf = zipfile.ZipFile(self.file_name)
            zf.extractall(output_path)
            return True
        except:
            return False
    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            zf = zipfile.ZipFile(self.file_name)
            zf.extract(file_name, output_path)
            return True
        except:
            return False
    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        """
        try:
            zf = zipfile.ZipFile(output_file_name, 'w')
            for file in files:
                zf.write(file)
            zf.close()
            return True
        except:
            return False