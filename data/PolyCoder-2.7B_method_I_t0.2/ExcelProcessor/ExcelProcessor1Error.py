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
        excel_file = openpyxl.open_workbook(file_name)

        # Read the data
        data = []
        for row in excel_file:
            # Get the data
            data.append(row)

        # Close the file
        excel_file.close()

        return data




    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('Name', 'Age', 'Country'),
        >>>     ('John', 25, 'USA'),
        >>>     ('Alice', 30, 'Canada'),
        >>>     ('Bob', 35, 'Australia'),
        >>>     ('Julia', 28, 'Germany')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """
        # Open the file
        excel_file = openpyxl.open_workbook(file_name)

        # Write the data
        for row in data:
            # Write the row
            excel_file.write(row)

        # Close the file
        excel_file.close()





    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
        # Open the file
        excel_file = openpyxl.open_workbook(save_file_name)

        # Change the column
        for i in range(N):
            # Write the row
            excel_file.write(str(i))

        # Close the file
        excel_file.close()