import zipfile
class ZipFileProcessor: 
    def __init__(self, file_name):
        """
        Initialize file name
        :param file_name:string
        """
        self.file_name = file_name



    def read_zip_file(self):
        

        with zipfile.ZipFile(self.file_name, 'r') as zf:
            return zf.open(zf.namelist()[0])


    def extract_all(self, output_path):


    def extract_file(self, file_name, output_path):


    def create_zip_file(self, files, output_file_name):