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
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                yield row



    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            return 1




    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        >>> csvProcessor.process_csv_data(0,'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
        title = ''
        data = ''
        for i in range(0, N):
            title += 'a'
            data += '1'
            title += '_process'
            data += '2'
            title += '_process'
            data += '3'
            title += '_process'
            data += '4'
            title += '_process'
            data += '5'
            title += '_process'
            data += '6'
            title += '_process'
            data += '7'
            title += '_process'
            data += '8'
            title += '_process'
            data += '9'
            title += '_process'
            data += '10'
            title += '_process'
            data += '11'
            title += '_process'
            data += '12'
            title += '_process'
            data += '13'
            title += '_process'
            data += '14'
            title += '_process'
            data += '15'
            title += '_process'
            data += '16'
            title += '_process'
            data += '17'
            title += '_process'
            data += '18'
            title += '_process'
            data += '19'
            title += '_process'
            data += '20'
            title += '_process'
            data += '21'
            title += '_process'
            data += '22'
            title += '_process'
            data += '23'
            title += '_process'
            data += '24'
            title += '_process'
            data += '25'
            title += '_process'
            data += '26'
            title += '_process'
            data += '27'
            title += '_process'
            data += '28'
            title += '_process'
            data += '29'
            title += '_process'
            data += '30'
            title += '_process'
            data += '31'
            title += '_process'
            data +=