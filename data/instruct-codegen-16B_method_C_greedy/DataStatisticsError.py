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
        if isinstance(data, list):
            if len(data) == 0:
                return 0
            total = 0
            for num in data:
                total += num
            return round(total / len(data), 2)
        else:
            raise TypeError("data must be a list")

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
        n = len(data)
        if n % 2 == 0:
            return (data[n//2] + data[n//2-1])/2
        else:
            return data[n//2]

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:list, the mode
        """
        count = Counter(data)
        mode_data = [item for item, count in count.items() if count == max(count.values())]
        return mode_data