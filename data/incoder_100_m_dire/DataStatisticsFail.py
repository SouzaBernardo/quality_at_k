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
        average = sum(data) / len(data)
        return round(average, 2)


    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            median = (sorted_data[length//2-1] + sorted_data[length//2]) / 2
        else:
            median = sorted_data[length//2]
        return median


    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        counter = Counter(data)
        mode = list(counter.keys())[list(counter.values()).index(max(list(counter.values())))]
        return mode