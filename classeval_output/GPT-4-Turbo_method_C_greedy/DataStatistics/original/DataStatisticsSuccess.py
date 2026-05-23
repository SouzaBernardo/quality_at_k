from collections import Counter
class DataStatistics: 

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        return round(sum(data) / len(data), 2)
    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        data.sort()
        length = len(data)
        if length % 2 == 0:
            median1 = data[length//2]
            median2 = data[length//2 - 1]
            median = (median1 + median2)/2
        else:
            median = data[length//2]
        return round(median, 2)
    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        """
        counter = Counter(data)
        max_count = max(list(counter.values()))
        mode_val = [num for num, freq in counter.items() if freq == max_count]
        if len(mode_val) == len(data):
            print("No mode in the list")
        else:
            return mode_val
