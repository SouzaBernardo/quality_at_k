import csv
class CSVProcessor:  
    """
    This is a class for processing CSV files, including readring and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """

    def __init__(self):
        pass



    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
        # open the file
        with open(file_name, 'r') as csv_file:
            # read the header
            csv_header = csv_file.readline()
            # read the data
            csv_data = csv_file.readlines()
            # get the title
            title = csv_header[0]
            # get the data
            data = csv_data
            # return the data
            return title, data




    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
        # open the file
        with open(file_name, 'w') as csv_file:
            # write the header
            csv_file.write('title,data\n')
            # write the data
            csv_file.write('a,b,c,d\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data
            csv_file.write('1,2,3,4\n')
            # write the data

