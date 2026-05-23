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
    
        def corr(x, y):
            """
            Calculate the correlation coefficient between two sets of data.
            :param x: The first set of data, list.
            :param y: The second set of data, list.
            :return: The correlation coefficient, float.
            >>> corr([1, 2, 3], [4, 5, 6])
            0.9999999999999998
            >>> corr([1, 2, 3], [1, 2, 3])
            1
            >>> corr([1, 2, 3], [4, 5, 6, 7, 8])
            0.9999999999999998
            """
            sum_of_products = [x[i] * y[i] for i in range(len(x))]
            sum_of_squares = [x[i] ** 2 + y[i] ** 2 for i in range(len(x))]
            return sum_of_products / sum_of_squares
    
        return corr(data1, data2)



    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007
        >>> DataStatistics4.kurtosis([1, 2, 3, 4])
        -0.5
        >>> DataStatistics4.kurtosis([1, 2, 3, 4, 5, 6])
        -0.5
        >>> DataStatistics4.kurtosis([1, 2, 3, 4, 5, 6, 7, 8, 9])
        -1.5
        >>> DataStatistics4.kurtosis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        -1.5
        """
        def kurtosis_value(data):
            """
            Calculate the kurtosis of a set of data.
            :param data: The input data list, list.
            :return: The kurtosis, float.
            >>> kurtosis_value([1, 2, 3, 4])
            -0.5
            >>> kurtosis_value([1, 2, 3, 4, 5, 6])
            -0.5
            >>> kurtosis_value([1, 2, 3, 4, 5, 6, 7, 8, 9])
            -1.5
            >>> kurtosis_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            -1.5
            """
            kurtosis = 0
            if len(data) > 1:
                kurtosis = (sum(data)**4) / (sum((data - math.mean(data))**2)**2)
            return kurtosis
    
        return kurtosis_value(data)

