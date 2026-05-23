import csv
class CSVProcessor: 
    def __init__(self):
        pass





    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param data: list, list of lists containing the data
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        with open(file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)
        return 1