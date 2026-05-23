import csv
class CSVProcessor: 
    def __init__(self):
        pass



    def read_csv(self, file_name):
        

        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            title = next(reader)
            data = []
            for row in reader:
                data.append(row)
        return title, data


    def write_csv(self, data, file_name):


    def process_csv_data(self, N, save_file_name):