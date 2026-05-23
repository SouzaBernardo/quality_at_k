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
        # Calculate the sum of the squares of the differences between the data
        sum_diff = sum([(x - y)**2 for (x, y) in zip(data1, data2)])
        # Calculate the mean of the differences
        mean_diff = sum_diff / len(data1)
        # Calculate the standard deviation of the differences
        std_diff = math.sqrt(sum([(x - y)**3 for (x, y) in zip(data1, data2)]))
        # Calculate the skewness and kurtosis of the differences
         skewness = (mean_diff - std_diff) / std_diff
        kurtosis = (std_diff - mean_diff) / std_diff
        return math.sqrt( skewness**2 + kurtosis**2)