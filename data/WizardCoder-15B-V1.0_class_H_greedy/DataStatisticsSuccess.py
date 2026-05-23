from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        """
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            # if n is even, take the average of the middle two numbers
            return round((sorted_data[n//2 - 1] + sorted_data[n//2]) / 2, 2)
        else:
            # if n is odd, return the middle number
            return round(sorted_data[n//2], 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        """
        counter = Counter(data)
        max_count = max(counter.values())
        return [k for k, v in counter.items() if v == max_count]