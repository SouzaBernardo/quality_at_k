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
        # Convert the data list to a Counter object
        data_counter = collections.Counter(data)

        # Calculate the mean and return it
        mean = sum(data_counter) / len(data_counter)
        return mean

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        """
        # Convert the data list to a Counter object
        data_counter = collections.Counter(data)

        # Calculate the median and return it
        median = data_counter. median()
        return median