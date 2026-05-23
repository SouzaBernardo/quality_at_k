import math

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """


    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007

        """

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]

        """

    @staticmethod
    def mean(data):
        """
        Calculate the mean of a set of data.
        :param data: The input data list, list.
        :return: The mean, float.
        >>> DataStatistics4.mean([1, 2, 3])
        2.5

        """

    @staticmethod
    def median(data):
        """
        Calculate the median of a set of data.
        :param data: The input data list, list.
        :return: The median, float.
        >>> DataStatistics4.median([1, 2, 3])
        2.5

        """

    @staticmethod
    def mode(data):
        """
        Calculate the mode of a set of data.
        :param data: The input data list, list.
        :return: The mode, float.
        >>> DataStatistics4.mode([1, 2, 3])
        2.5

        """

    @staticmethod
    def variance(data):
        """
        Calculate the variance of a set of data.
        :param data: The input data list, list.
        :return: The variance, float.
        >>> DataStatistics4.variance([1, 2, 3])
        1.8333333333333333

        """

    @staticmethod
    def standard_deviation(data):
        """
        Calculate the standard deviation of a set of data.
        :param data: The input data list, list.
        :return: The standard deviation, float.
        >>> DataStatistics4.standard_deviation([1, 2, 3])
        1.1803398874989484

        """

    @staticmethod
    def variance_of_mean(data):
        """
        Calculate the variance of the mean of a set of data.
        :param data: The input data list, list.
        :return: The variance of the mean, float.
        >>> DataStatistics4.variance_of_mean([1, 2, 3])
        1.8333333333333333

        """

    @staticmethod
    def standard_deviation_of_mean(data):
        """
        Calculate the standard deviation of the mean of a set of data.
        :param data: The input data list, list.
        :return: The standard deviation of the mean, float.
        >>> DataStatistics4.standard_deviation_of_mean([1, 2, 3])
        1.1803398874989484

        """

    @staticmethod
    def variance_of_mode(data):
        """
        Calculate the variance of the mode of a set of data.
        :param data: The input data list, list.
        :return: The variance of the mode, float.
        >>> DataStatistics4.variance_of_mode([1, 2, 3])
        1.8333333333333333

        """

    @staticmethod
    def standard_deviation_of_mode(data):
        """
        Calculate the standard deviation of the mode of a set of data.
        :param data: The input data list, list.
        :return: The standard deviation of the mode, float.
        >>> DataStatistics4.standard_deviation_of_mode([1, 2, 3])
        1.1803398874989484

        """

    @staticmethod
    def variance_of_median(data):
        """
        Calculate the variance of the median of a set of data.
        :param data: The input data list, list.
        :return: The variance of the median, float.
        >>> DataStatistics4.variance_of_median([1, 2, 3])
        1.8333333333333333

        """

    @staticmethod
    def standard_deviation_of_median(data):
        """
        Calculate the standard deviation of the median of a set of data.
        :param data: The input data list, list.
        :return: The standard deviation of the median, float.
        >>> DataStatistics4.standard_deviation_of_median([1, 2, 3])
        1.1803398874989484

        """

    @staticmethod
    def variance_of_mode_of_median(data):
        """
        Calculate the variance of the mode of the median of a set of data.
        :param data: The input data list, list.
        :return: The variance of the mode of the median, float.
        >>> DataStatistics4.variance_of_mode_of_median([1, 2, 3])
        1.8333333333333333

        """

    @staticmethod
    def standard_deviation_of_mode_of_median(data):
        """
        Calculate the standard deviation of the mode of the median of a set of data.
        :param data: The input data list, list.
        :return: The standard deviation of the mode of the median, float.
        >>> DataStatistics4.standard_deviation_of_mode_of_median([1, 2, 3])
        1.1803398874989484

        """

    @staticmethod
    def variance_of_mode_of_mode_of_median(data):
        """
        Calculate the variance of the mode of the mode of the median of a set of data.
        :param data: The input data list, list.
        :return: The variance of the mode of the mode of the median, float.
        >>> DataStatistics4.variance_of_mode_of_mode_of_median([1, 2, 3])
        1.8333333333333333

        """

    @staticmethod
    def standard_deviation_of_mode_of_mode_of_median(data):
        """
        Calculate the standard deviation of the mode of the mode of the median of a set of data.
        :param data: The input data list, list.
        :return: The standard deviation of the mode of the mode of the median, float.
        >>> DataStatistics4.standard_deviation_of_mode_of_mode_of_median([1, 2, 3])
        1.1803398874989484

        """

    @staticmethod
    def variance_of_mode_of_mode_of_mode_of_median(data):
        """
        Calculate the variance of the mode of the mode of the mode of the median of a set of data.
        :param data: The input data list, list.
        :return: The variance of the mode of the mode of the mode of the median, float.
        >>> DataStatistics4.variance_of_mode_of_mode_of_mode_of_median([1, 2, 3])
        1.83333333333333