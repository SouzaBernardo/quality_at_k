import csv

class CSVProcessor:
    """
    This is a class for processing CSV files, including reading and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """

    def __init__(self):
        self._file = None

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        """
        self._file = open(file_name, 'r')
        self._data = []
        self._title = []
        self._process_data = False
        self._save_data = False
        self._next_row = 1
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_file = file_name
        self._save_data = False
        self._next_column = 0
        self._column_count = 0
        self._column_index = 0
        self._data_count = 0
        self._process_data = True
        self._next_row = 0
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_file = self._file
        self._save_data = self._file.read()
        self._next_column = 0
        self._column_count = 0
        self._column_index = 0
        self._data_count = 0
        self._next_row = 0
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_file.close()

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param data: list, the data to be written
        :param file_name: str, name of the csv file
        """
        self._next_row = 1
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_data = False
        self._next_column = 0
        self._column_count = 0
        self._column_index = 0
        self._data_count = 0
        self._next_row = 0
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_file = file_name
        self._save_data = self._file.write(data)
        self._next_column = 0
        self._column_count = 0
        self._column_index = 0
        self._data_count = 0
        self._next_row = 0
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_file.close()

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        """
        self._next_row = 1
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_data = False
        self._next_column = 0
        self._column_count = 0
        self._column_index = 0
        self._data_count = 0
        self._next_row = 0
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0
        self._title_index = 0
        self._save_file = save_file_name
        self._save_data = self._file.read()
        self._next_column = 0
        self._column_count = 0
        self._column_index = 0
        self._data_count = 0
        self._next_row = 0
        self._current_column = 0
        self._current_row = 0
        self._current_column_index = 0
        self._data_index = 0