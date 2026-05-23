import math
class DataStatistics4: 


    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        """
        n = len(data1)
        if n!= len(data2):
            raise ValueError("The two lists must have the same length.")
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)) * sum((data2[i] - mean2) ** 2 for i in range(n)))
        return numerator / denominator


    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum([(x - mean) ** 2 for x in data]) / n
        standard_deviation = math.sqrt(variance)
        skewness = sum([(x - mean) ** 3 for x in data]) / (n * standard_deviation ** 3)
        return skewness

    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum([(x - mean) ** 2 for x in data]) / n
        std_dev = math.sqrt(variance)
        kurt = sum([(x - mean) ** 4 for x in data]) / (variance ** 2)
        kurt -= 3
        return kurt

    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        """
        pdf_list = []
        for x in data:
            pdf_list.append(math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi)))
        return pdf_list