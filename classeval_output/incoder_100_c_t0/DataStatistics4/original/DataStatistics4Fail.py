class DataStatistics4:  
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """


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
        
    def covariance(data1, data2):
        """
        Calculate the covariance of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The covariance coefficient, float.
        >>> DataStatistics4.covariance([1, 2, 3], [4, 5, 6])
        5.000000000000001

        """

    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """

    @staticmethod
        
    def kurtosis_excess(data):
        """
        Calculate the kurtosis excess of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis excess, float.
        >>> DataStatistics4.kurtosis_excess([1, 20, 100])
        -1.5000000000000007

        """

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
    def cdf(data, mu, sigma):
        """
        Calculate the cumulative distribution function (CDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The cumulative distribution function (CDF), list.
        >>> DataStatistics4.cdf([1, 2, 3], 1, 1)
        [0.5, 0.5, 0.0]

        """

<|/ file |>
