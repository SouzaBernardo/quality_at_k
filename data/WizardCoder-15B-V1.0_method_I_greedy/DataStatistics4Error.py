import math
class DataStatistics4:  
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """







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