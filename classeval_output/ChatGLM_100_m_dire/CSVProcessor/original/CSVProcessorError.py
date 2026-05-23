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
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            data = []
            for row in reader:
                data.append(row[0])
            return header, data

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :param data: list of dictionaries, data to be written to the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
        if len(data) == 0:
            return 0
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        return 1

    def process_csv_data(self, N, save_file_name):
        title =''.join([str(i) for i in range(N)])
        data = [[title]] * N
        data[N-1] = [['_process' if i % 2 == 0 else str(i) for i in range(N-1)]]
        data[N-2] = [['_process' if i % 2 == 0 else str(i) for i in range(N-2)]]
        data[N-3] = [['_process' if i % 2 == 0 else str(i) for i in range(N-3)]]
        
        with open(save_file_name, 'w') as f:
            f.write('\n'.join([str(title) for title in data]))
            f.write('\n'.join([str(data[i][j]) for i in range(N-1) for j in range(N-1)]))
            f.write('\n'.join([str(data[i][j]) for i in range(N-2) for j in range(N-2)]))
            f.write('\n'.join([str(data[i][j]) for i in range(N-3) for j in range(N-3)]))
        
        return 1