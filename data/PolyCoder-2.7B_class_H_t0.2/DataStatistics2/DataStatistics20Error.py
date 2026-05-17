import numpy as np

class DataStatistics2:
    """
    This is a class for performing data statistics, supporting to get the sum, minimum, maximum, variance, standard deviation, and correlation of a given dataset.
    """

    def __init__(self, data):
        """
        Initialize Data List
        :param data:list
        """
        self.data = np.array(data)

    def get_sum(self):
        """
        Calculate the sum of data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_sum()
        10
        """

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min()
        1
        """

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_max()
        4
        """

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """

    def get_mean(self):
        """
        Calculate the mean of the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_mean()
        2
        """

    def get_std_dev(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev()
        1.25
        """

    def get_min_max(self):
        """
        Calculate the minimum and maximum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min_max()
        1
        """

    def get_std_dev_min(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_min()
        1.25
        """

    def get_std_dev_max(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_max()
        1.25
        """

    def get_std_dev_variance(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_variance()
        1.25
        """

    def get_std_dev_mean(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_mean()
        2
        """

    def get_std_dev_min_max(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_min_max()
        2
        """

    def get_std_dev_variance_min(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_variance_min()
        2
        """

    def get_std_dev_variance_max(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_dev_variance_max()
        2
        """

    def get_std_dev_mean_max(self):
        """
        Calculate the standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1