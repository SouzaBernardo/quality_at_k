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
        data = list(data)
        if len(data) == 0:
            return 0.0
        else:
            total = sum(data)
            return total / len(data)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        data = list(data)
        if len(data) % 2 == 0:
            return (data[len(data) / 2 - 1] + data[len(data) / 2]) / 2
        else:
            return data[len(data) / 2]

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        data_set = list(data)
        if len(data_set) < 2:
            return None
        mode = max(data_set, key=data_set.count)
        return mode