import openpyxl
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
        # Open the file
        file_handle = openpyxl.open_file(file_name)

        # Get the sheets
        sheets = file_handle.sheet_names

        # Get the sheets
        sheets_list = []
        for sheet in sheets:
            sheet_name = sheet
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")
            sheet_name = sheet_name.replace(" ", "_")
            sheet_name = sheet_name.replace("'", "")
            sheet_name = sheet_name.replace("\"", "")



