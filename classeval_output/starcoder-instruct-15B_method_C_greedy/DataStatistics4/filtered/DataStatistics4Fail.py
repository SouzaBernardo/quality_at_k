import math
class DataStatistics4: 


    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        -0.0

        """
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        std_dev1 = math.sqrt(sum([(x - mean1) ** 2 for x in data1]) / n)
        std_dev2 = math.sqrt(sum([(x - mean2) ** 2 for x in data2]) / n)
        cov = sum([(x - mean1) * (y - mean2) for x, y in zip(data1, data2)]) / n
        return cov / (std_dev1 * std_dev2)

    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """
        mean = sum(data) / len(data)
        std = math.sqrt(sum([(x - mean) ** 2 for x in data]) / len(data))

        return sum([(x - mean) ** 3 for x in data]) / len(data) / std ** 3

    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007

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
        return [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) for x in data]