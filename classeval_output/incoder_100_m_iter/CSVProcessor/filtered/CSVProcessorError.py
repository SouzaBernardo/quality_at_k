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
        title = []
        data = []
        with open(file_name) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                title.append(row[0])
                data.append(row[1:])
        return title, data