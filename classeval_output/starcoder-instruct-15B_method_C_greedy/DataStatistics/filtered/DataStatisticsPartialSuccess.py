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
        return sum(data) / len(data)

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
            middle1 = data[length // 2 - 1]
            middle2 = data[length // 2]
            median_value = (middle1 + middle2) / 2
        else:
            median_value = data[length // 2]
        return median_value


    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        count = Counter(data)
        return [elem for elem, freq in count.items() if freq == count.most_common(1)[0][1]]