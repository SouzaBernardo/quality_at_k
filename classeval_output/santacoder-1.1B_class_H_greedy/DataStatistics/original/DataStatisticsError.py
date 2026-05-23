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

    def variance(self, data):
        """
        Calculate the variance of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the variance
        >>> ds = DataStatistics()
        >>> ds.variance([1, 2, 3, 4, 5])
        2.00
        """

    def standard_deviation(self, data):
        """
        Calculate the standard deviation of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the standard deviation
        >>> ds = DataStatistics()
        >>> ds.standard_deviation([1, 2, 3, 4, 5])
        2.00
        """

    def skewness(self, data):
        """
        Calculate the skewness of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the skewness
        >>> ds = DataStatistics()
        >>> ds.skewness([1, 2, 3, 4, 5])
        0.00
        """

    def kurtosis(self, data):
        """
        Calculate the kurtosis of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the kurtosis
        >>> ds = DataStatistics()
        >>> ds.kurtosis([1, 2, 3, 4, 5])
        0.00
        """

    def entropy(self, data):
        """
        Calculate the entropy of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the entropy
        >>> ds = DataStatistics()
        >>> ds.entropy([1, 2, 3, 4, 5])
        0.00
        """

    def z_score(self, data):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score([1, 2, 3, 4, 5])
        0.00
        """

    def z_score_with_mean(self, data, mean):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean([1, 2, 3, 4, 5], 3)
        0.00
        """

    def z_score_with_mean_and_standard_deviation(self, data, mean, standard_deviation):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :param standard_deviation:float, the standard deviation
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean_and_standard_deviation([1, 2, 3, 4, 5], 3, 2)
        0.00
        """

    def z_score_with_mean_and_standard_deviation_and_skewness(self, data, mean, standard_deviation, skewness):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :param standard_deviation:float, the standard deviation
        :param skewness:float, the skewness
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean_and_standard_deviation_and_skewness([1, 2, 3, 4, 5], 3, 2, 0.5)
        0.00
        """

    def z_score_with_mean_and_standard_deviation_and_kurtosis(self, data, mean, standard_deviation, kurtosis):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :param standard_deviation:float, the standard deviation
        :param kurtosis:float, the kurtosis
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean_and_standard_deviation_and_kurtosis([1, 2, 3, 4, 5], 3, 2, 3)
        0.00
        """

    def z_score_with_mean_and_standard_deviation_and_entropy(self, data, mean, standard_deviation, entropy):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :param standard_deviation:float, the standard deviation
        :param entropy:float, the entropy
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean_and_standard_deviation_and_entropy([1, 2, 3, 4, 5], 3, 2, 0.5)
        0.00
        """

    def z_score_with_mean_and_standard_deviation_and_skewness_and_kurtosis(self, data, mean, standard_deviation, skewness, kurtosis):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :param standard_deviation:float, the standard deviation
        :param skewness:float, the skewness
        :param kurtosis:float, the kurtosis
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean_and_standard_deviation_and_skewness_and_kurtosis([1, 2, 3, 4, 5], 3, 2, 0.5, 3)
        0.00
        """

    def z_score_with_mean_and_standard_deviation_and_skewness_and_kurtosis_and_entropy(self, data, mean, standard_deviation, skewness, kurtosis, entropy):
        """
        Calculate the z-score of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :param mean:float, the mean value
        :param standard_deviation:float, the standard deviation
        :param skewness:float, the skewness
        :param kurtosis:float, the kurtosis
        :param entropy:float, the entropy
        :return:float, the z-score
        >>> ds = DataStatistics()
        >>> ds.z_score_with_mean_and_standard_deviation_and_skewness_and_kurtosis_and_entropy([1, 2, 3, 4, 5], 3, 2, 0.5, 3, 0.5)
        0.00
        """

    def z_score_with_mean_and_standard_deviation_and_skewness_and_kurtosis_and_entropy_and_z_score(self, data, mean, standard_deviation, skewness, kurtosis, entropy, z_score):
        """
        Calculate the z-score of a group of data, accurate