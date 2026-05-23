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
        try:
            with open(file_name, 'r') as csv_file:
                reader = csv.reader(csv_file)
                title = next(reader)
                data = [row for row in reader]
                return title, data
        except Exception as e:
            print(f"Error reading csv file: {e}")
            return None, None

    def write_csv(data, file_name):
        """
        Write data into a csv file.
    
        :param data: list, list of lists, each inner list represents a row
        :param file_name: str, name of the csv file
        :return: int, 1 if success, 0 otherwise
        """
        try:
            with open(file_name, 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data[0])
                for row in data:
                    writer.writerow(row)
                return 1
        except Exception as e:
            print(f"Error writing csv file: {e}")
            return 0