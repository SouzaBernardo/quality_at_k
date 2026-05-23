import math

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0

        """

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """

    @staticmethod
    def variance(data):
        """
        calculates the variance of the given list.
        :param data: the given list, list.
        :return: the variance of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance([1, 2, 3, 4])
        2.0

        """

    @staticmethod
    def skewness(data):
        """
        calculates the skewness of the given list.
        :param data: the given list, list.
        :return: the skewness of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.skewness([1, 2, 3, 4])
        0.0

        """

    @staticmethod
    def kurtosis(data):
        """
        calculates the kurtosis of the given list.
        :param data: the given list, list.
        :return: the kurtosis of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.kurtosis([1, 2, 3, 4])
        0.0

        """

    @staticmethod
    def entropy(data):
        """
        calculates the entropy of the given list.
        :param data: the given list, list.
        :return: the entropy of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.entropy([1, 2, 3, 4])
        0.0

        """

    @staticmethod
    def variance_covariance(data):
        """
        calculates the variance and covariance of the given list.
        :param data: the given list, list.
        :return: the variance and covariance of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance_covariance([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def variance_covariance_skewness(data):
        """
        calculates the variance and covariance and skewness of the given list.
        :param data: the given list, list.
        :return: the variance and covariance and skewness of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance_covariance_skewness([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def variance_covariance_kurtosis(data):
        """
        calculates the variance and covariance and kurtosis of the given list.
        :param data: the given list, list.
        :return: the variance and covariance and kurtosis of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance_covariance_kurtosis([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def variance_covariance_entropy(data):
        """
        calculates the variance and covariance and entropy of the given list.
        :param data: the given list, list.
        :return: the variance and covariance and entropy of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance_covariance_entropy([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def variance_covariance_skewness_kurtosis(data):
        """
        calculates the variance and covariance and skewness and kurtosis of the given list.
        :param data: the given list, list.
        :return: the variance and covariance and skewness and kurtosis of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance_covariance_skewness_kurtosis([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def variance_covariance_skewness_entropy(data):
        """
        calculates the variance and covariance and skewness and entropy of the given list.
        :param data: the given list, list.
        :return: the variance and covariance and skewness and entropy of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.variance_covariance_skewness_entropy([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """

    @staticmethod
    def variance_covariance_kurtosis_entropy(data):
        """
        calculates the variance and covariance and kurtosis and entropy of the given list.
        :param data: the given list, list.
        :return: the variance and covariance and kur