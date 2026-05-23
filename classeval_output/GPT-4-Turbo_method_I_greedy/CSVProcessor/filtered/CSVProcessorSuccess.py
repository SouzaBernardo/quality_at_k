import csv
class CSVProcessor: 
    def __init__(self):
        pass


    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        """
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            title = data[0]
            data = data[1:]
        return title, data
    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param data: list, data to be written into the csv file
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except Exception as e:
            print("An error occurred while writing to the CSV file: ", e)
            return 0
    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            title, data = self.read_csv(save_file_name)
            processed_data = [[row[N].upper()] for row in data]
            new_file_name = save_file_name.split('.')[0] + '_process.csv'
            self.write_csv([title] + processed_data, new_file_name)
            return 1
        except Exception as e:
            print("An error occurred while processing the CSV file: ", e)
            return 0