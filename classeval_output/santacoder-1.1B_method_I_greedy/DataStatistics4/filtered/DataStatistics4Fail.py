import math
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
        if len(data1)!= len(data2):
            raise ValueError("The two sets of data must have the same length.")
        else:
            sum_of_squares = 0
            for i in range(len(data1)):
                sum_of_squares += (data1[i] - data2[i]) ** 2
            sum_of_products = 0
            for i in range(len(data1)):
                sum_of_products += (data1[i] * data2[i])
            return sum_of_products / math.sqrt(sum_of_squares)


    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """
        if len(data) == 0:
            raise ValueError("The input data list must have at least one element.")
        else:
            mean = sum(data) / len(data)
            sum_of_products = 0
            for i in range(len(data)):
                sum_of_products += (data[i] - mean) ** 3
            return sum_of_products / (len(data) * (len(data) - 1))



    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007

        """
        if len(data) == 0:
            raise ValueError("The input data list must have at least one element.")
        else:
            mean = sum(data) / len(data)
            sum_of_products = 0
            for i in range(len(data)):
                sum_of_products += (data[i] - mean) ** 4
            return sum_of_products / (len(data) * (len(data) - 1) * (len(data) - 2))




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
        if len(data) == 0:
            raise ValueError("The input data list must have at least one element.")
        else:
            pdf = []
            for i in range(len(data)):
                pdf.append((1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-(data[i] - mu) ** 2 / (2 * sigma ** 2)))
            return pdf