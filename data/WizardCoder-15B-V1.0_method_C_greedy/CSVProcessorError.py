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
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            title = next(reader)
            data = [row for row in reader]
        return title, data

    def write_csv(self, data, file_name):
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
        return 1

    def process_csv_data(self, N, save_file_name):
        # Read the CSV file
        title, data = self.read_csv(save_file_name)
        # Extract the N th column and capitalize each element
        new_data = [[row[N].upper()] for row in data]
        # Save the new data and title to a new CSV file
        new_file_name = save_file_name.split('.')[0] + '_process.csv'
        self.write_csv([title[:N] + title[N+1:], new_data], new_file_name)
        return 1