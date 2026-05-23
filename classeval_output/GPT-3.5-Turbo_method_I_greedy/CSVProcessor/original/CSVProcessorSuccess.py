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
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            title = rows[0]
            data = rows[1:]
        return title, data


    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
            return 1
        except Exception as e:
            print(f"Error writing CSV file: {e}")
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
            # Read the original CSV file
            title, data = self.read_csv(save_file_name)
            
            # Extract the Nth column and capitalize the values
            processed_data = [[row[N].upper()] for row in data]
            
            # Create the new file name
            new_file_name = save_file_name.split('.')[0] + '_process.csv'
            
            # Write the processed data to the new CSV file
            success = self.write_csv([title, *processed_data], new_file_name)
            
            return success
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            return 0
    