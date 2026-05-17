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

    def get_correlation_std_deviation(self):
        """
        Calculate correlation std deviation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_std_deviation()
        0.5
        """

    def get_correlation_min(self):
        """
        Calculate correlation min
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_min()
        1.0
        """

    def get_correlation_max(self):
        """
        Calculate correlation max
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_max()
        4.0
        """

    def get_correlation_mean(self):
        """
        Calculate correlation mean
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_mean()
        1.0
        """

    def get_correlation_std_deviation(self):
        """
        Calculate correlation std deviation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_std_deviation()
        0.5
        """

    def get_correlation_min_max(self):
        """
        Calculate correlation min and max
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_min_max()
        (1.0, 4.0)
        """

    def get_correlation_min_max_std_deviation(self):
        """
        Calculate correlation min and max std deviation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_min_max_std_deviation()
        (0.5, 0.5)
        """

    def get_correlation_min_max_mean(self):
        """
        Calculate correlation min and max mean
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_min_max_mean()
        (1.0, 4.0)
        """

    def get_correlation_min_max_std_deviation(self):
        """
        Calculate correlation min and max std deviation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_min_max_std_deviation()
        (0.5, 0.5)
        """

    def get_correlation_min_max_mean_std_deviation(self):
        """
        Calculate correlation min and max mean and std deviation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation_min_max_mean_std_deviation()
        (1.0, 4.0)
        """

    def get_correlation_min_max_mean_std_deviation_mean(self):
        """
        Calculate correlation min and max mean and std deviation
        :return:float
    