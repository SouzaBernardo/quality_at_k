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

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """

    def mode_percent(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_mean(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_mean([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_median(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_median([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_mean_median(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_mean_median([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_median_mean(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_median_mean([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_median_median(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_median_median([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_median_mean_median(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_median_mean_median([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_mean_median_mean(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_mean_median_mean([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_mean_median_median(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_mean_median_median([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_mean_median_mean_median(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode_percent_mean_median_mean_median([2, 2, 3, 3, 4])
        [2.00, 3.00]
        """

    def mode_percent_mean_median_mean_median_mean(self, data):
        """
        Calculate the mode of a set of data, accurate to two digits after the Decimal separator
        :param data:list, data list
  