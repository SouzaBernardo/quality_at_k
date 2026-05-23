import openpyxl
class ExcelProcessor: 
    def __init__(self):
        pass



    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
        workbook = openpyxl.load_workbook(file_name)
        worksheet = workbook.active
        data = []
        for row in worksheet:
            data.append([cell.value for cell in row])
        return data




    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
        wb = openpyxl.load_workbook(save_file_name)
        sheet = wb.active
        for row in sheet:
            for cell in row:
                if cell.column == N:
                    cell.value = cell.value.upper()
        wb.save(output_file_name)
        return (success, output_file_name)