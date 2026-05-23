import csv
class CSVProcessor: 
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
            with open(file_name, 'r') as csvfile:
                reader = csv.reader(csvfile)
                title = next(reader)
                data = [row for row in reader]
                return title, data
        except Exception as e:
            print(f"Error reading csv file: {e}")
            return None, None

    def write_csv(data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
        try:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data[0])
                for row in data[1:]:
                    writer.writerow(row)
                print("Data written successfully to", file_name)
                return 1
        except Exception as e:
            print(f"Error writing data to {file_name}: {e}")
            return 0

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
        >>> csvProcessor.process_csv_data(0, 'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
        try:
            # Open the file
            with open(file_name, 'r') as f:
                # Read the file
                reader = csv.reader(f)
                # Get the title and data
                title = next(reader)
                data = next(reader)
                # Only keep the Nth column
                for i in range(N):
                    data = [row[i] for row in data]
                # Capitalize the first letter of each column
                data = [title[i].upper() + x for i, x in enumerate(data)]
                # Write the new data to a new file
                with open(save_file_name + '_process', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(title)
                    writer.writerows(data)
                return 1
        except Exception as e:
            return 0