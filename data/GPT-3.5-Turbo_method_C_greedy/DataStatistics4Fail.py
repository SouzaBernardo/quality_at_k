import math
class DataStatistics4: 


    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data, list.
        :param data2: The second set of data, list.
        :return: The correlation coefficient, float.
        """
        n = len(data1)
        mean_data1 = sum(data1) / n
        mean_data2 = sum(data2) / n
    
        numerator = sum((x - mean_data1) * (y - mean_data2) for x, y in zip(data1, data2))
        denominator = math.sqrt(sum((x - mean_data1) ** 2 for x in data1)) * math.sqrt(sum((y - mean_data2) ** 2 for y in data2))
    
        correlation_coefficient = numerator / denominator
        return correlation_coefficient
    

    @staticmethod
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
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)
        skewness = sum((x - mean) ** 3 for x in data) / (n * std_dev ** 3)
        return skewness
    

    @staticmethod
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
        variance = sum((x - mean) ** 2 for x in data) / n
        kurtosis = sum((x - mean) ** 4 for x in data) / (variance ** 2)
        return kurtosis
    

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        """
        pdf_values = []
        for x in data:
            exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
            pdf = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(exponent)
            pdf_values.append(pdf)
        return pdf_values