Here is the completed ExcelProcessor class:
```python
import openpyxl

class ExcelProcessor:
    """
    This is a class for processing Excel files, including reading and writing Excel data, as well as processing specific operations and saving as a new Excel file.
    """

    def __init__(self):
        self.file_name = None

    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
        return self.file_name, []

    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        """
        if self.file_name is None:
            self.file_name, data = self.read_excel(file_name)
        else:
            self.file_name, data = self.read_excel(file_name)
        return 1, data

    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        """
        if N == 1:
            data = [d.upper() for d in data]
        else:
            data = [d[N-1].upper() for d in data]
        return N, save_file_name

    def save_excel(self, save_file_name):
        """
        Save the Excel file as a new Excel file
        :param save_file_name: str, Excel file name to save as
        """
        self.file_name = save_file_name
        openpyxl.save_workbook(self.file_name, self.file_name)
```