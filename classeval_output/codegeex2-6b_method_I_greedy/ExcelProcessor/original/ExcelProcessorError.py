import openpyxl
class ExcelProcessor:  
    """
    This is a class for processing excel files, including readring and writing excel data, as well as processing specific operations and saving as a new excel file.
    """

    def __init__(self):
        pass



    def read_excel(self, file_name):
        
        wb = openpyxl.load_workbook(file_name)
        ws = wb.active
        data = []
        for row in ws.rows:
            data.append([cell.value for cell in row])
        return data



    def write_excel(self, file_name, data):


    def write_excel(self, data, file_name):


    def process_excel_data(self, N, save_file_name):
