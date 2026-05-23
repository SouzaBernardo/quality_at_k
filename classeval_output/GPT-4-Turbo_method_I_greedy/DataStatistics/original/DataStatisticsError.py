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
            return round((data[length // 2 - 1] + data[length // 2]) / 2, 2)
        else:
            return round(data[length // 2], 2)
    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:list, the mode(s)
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        counter = Counter(data)
        max_count = max(counter.values())
        mode_values = [k for k, v in counter.items() if v == max_count]
        return mode_values
    
