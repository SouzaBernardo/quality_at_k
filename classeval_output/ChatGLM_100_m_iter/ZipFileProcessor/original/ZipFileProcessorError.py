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





    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
        for file in zfp.listdir():
            if file.endswith(".zip"):
                output_path = os.path.join(output_path, file)
                zfp.extract(output_path)
                return True
        return False

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        if file_name in self.files:
            output_path = os.path.join(output_path, file_name)
            zfp.extract(output_path)
            return True
        else:
            print(f"File {file_name} not found in the zip file.")
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        """
        self.files = files
        output_path = os.path.join(self.output_path, output_file_name)
        zfp.create_zipfile(output_path)