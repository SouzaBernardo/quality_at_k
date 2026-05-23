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
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        >>> decompressed_data = file.read()
        >>> print(decompressed_data)
        """
        try:
            decompressed_data = self.decompress(file)
            return decompressed_data
        except:
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
        for file in zfp.files:
            file.extract(output_path)
        return True

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            with self.open(file_name) as zipfile:
                file_content = zipfile.read()
                output_path = os.path.join(output_path, file_name)
                zipfile.close()
                return True
        except Exception as e:
            print(f"Error extracting file: {e}")
            return False

