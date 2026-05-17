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
        """
        pass


    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
        return True


    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_file("bbb.txt", "result/aaa")
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if not os.path.exists(output_path):
            return False
        if not os.path.isfile(file_name):
            return False
        if not os.path.isfile(output_path):
            return False
        if not os.path.isfile(output_path + "/" + file_name):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.bz2"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip"):
            return False
        if not os.path.isfile(output_path + "/" + file_name + ".zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.zip.bz2"):
     

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
        """
        zip_file = zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED)
        for file_name in files:
            zip_file.write(file_name, os.path.join(output_path, file_name))
        zip_file.close()
        return True