from collections import Counter
class DataStatistics: 


    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        """
        if len(data) == 0:
            return 0
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        """
        n = len(data)
        if n == 0:
            return 0
        sorted_data = sorted(data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        """
        counter = Counter(data)
        max_freq = max(counter.values())
        modes = [k for k, v in counter.items() if v == max_freq]
        return modes