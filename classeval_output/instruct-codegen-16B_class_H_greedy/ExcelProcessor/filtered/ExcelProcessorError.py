class ExcelProcessor:
    """
    This is a class for processing excel files, including readring and writing excel data, as well as processing specific operations and saving as a new excel file.
    """
    def __init__(self):
        pass
    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
        # open the excel file
        wb = openpyxl.load_workbook(file_name)
        # get the active sheet
        sheet = wb.active
        # get the data from the sheet
        data = []
        # loop through the rows
        for row in sheet.rows:
            row_data = []
            # loop through the columns
            for cell in row:
                row_data.append(cell.value)
            # append the row data
            data.append(row_data)
        # return the data
        return data
    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        """
        # open the excel file
        wb = openpyxl.Workbook()
        # create a new sheet
        sheet = wb.create_sheet('Processed Data')
        # loop through the data
        for row in data:
            # loop through the columns
            for col, val in enumerate(row):
                # write the data to the sheet
                sheet.cell(row=col+1, column=1).value = val
        # save the file
        wb.save(file_name)
        return 0
    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        """
        # open the source file
        wb = openpyxl.load_workbook(save_file_name)
        # get the active sheet
        sheet = wb.active
        # get the data from the sheet
        data = []
        # loop through the rows
        for row in sheet.rows:
            row_data = []
            # loop through the columns
            for cell in row:
                row_data.append(cell.value)
            # append the row data
            data.append(row_data)
        # get the column number
        col_num = data[0].index(N)
        # loop through the rows
        for row in data:
            # loop through the columns
            for col, val in enumerate(row):
                # write the data to the sheet
                if col == col_num:
                    row[col] = str(val).upper()
        # save the file
        wb.save(save_file_name)
        return (0, save_file_name)