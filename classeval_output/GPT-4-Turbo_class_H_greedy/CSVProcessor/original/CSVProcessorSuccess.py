```python
import csv

class CSVProcessor:
    """
    This is a class for processing CSV files, including reading and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """

    def __init__(self):
        pass

    def read_csv(self, file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            title = data[0]
            data = data[1:]
        return title, data

    def write_csv(self, data, file_name):
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except:
            return 0

    def process_csv_data(self, N, save_file_name):
        title, data = self.read_csv(save_file_name)
        processed_data = [[row[N].upper()] for row in data]
        save_file_name = save_file_name.split('.')[0] + '_process.csv'
        return self.write_csv([title] + processed_data, save_file_name)
```