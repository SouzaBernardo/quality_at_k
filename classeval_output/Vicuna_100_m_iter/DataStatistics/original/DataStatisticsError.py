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
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        if not isinstance(data, list):
            raise TypeError("data should be a list")
        if len(data) == 0:
            raise ValueError("data should not be empty")
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
        if not isinstance(data, list):
            raise TypeError("data should be a list")
        if len(data) == 0:
            raise ValueError("data should not be empty")
        n = len(data)
        if n % 2 == 0:
            return (sum(data) / n) / 2.0
        else:
            return (sum(data) / (n + 1)) / 2.0