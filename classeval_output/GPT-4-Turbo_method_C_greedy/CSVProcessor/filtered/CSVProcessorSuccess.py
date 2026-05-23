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
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
            return 1
        except Exception as e:
            print("Error writing to csv file: ", e)
            return 0
    def process_csv_data(self, N, save_file_name):
        try:
            title, data = self.read_csv(save_file_name)
            processed_data = [[row[N].upper()] for row in data]
            new_file_name = save_file_name.split('.')[0] + '_process.csv'
            self.write_csv([title] + processed_data, new_file_name)
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0