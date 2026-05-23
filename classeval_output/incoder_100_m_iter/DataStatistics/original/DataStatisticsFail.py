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
        average = sum(data) / len(data)
        return round(average, 2)
