import math
class Statistics3:  
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """



    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5
    
        """
    

    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        if len(data) > 0:
            return [data.count(item) for item in data]
        else:
            return []

    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
            1.0
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6, 7])
            0.5
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6, 7, 8])
            0.3
        """
        if len(x) != len(y):
            raise ValueError("The lists must have the same length.")
    
        sum_xy = sum([x[i] * y[i] for i in range(len(x))])
        sum_x = sum([x[i] for i in range(len(x))])
        sum_y = sum([y[i] for i in range(len(y))])
    
        return sum_xy / (sum_x * sum_y)

    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
        return float(sum(data) / len(data))

    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
    
        """
        if len(data) != 2:
            raise ValueError("The list must have exactly 2 elements.")
    
        if len(data[0]) != 2:
            raise ValueError("The elements of the first list must have exactly 2 elements.")
    
        if len(data[1]) != 2:
            raise ValueError("The elements of the second list must have exactly 2 elements.")
    
        if data[0][0] == data[0][1] or data[0][0] == data[0][2] or data[0][1] == data[0][2] or \
           data[1][0] == data[1][1] or data[1][0] == data[1][2] or data[1][1] == data[1][2]:
            raise ValueError("The elements of the list must be different.")
    
        if data[0][0] == data[1][0]:
            corr = 1.0
        else:
            corr = float(data[0][0] * data[1][1] - data[0][1] * data[1][0]) / (float(data[0][0] - data[1][0]) * float(data[0][1] - data[1][1]))
    
        return [[corr, corr, corr], [corr, corr, corr], [corr, corr, corr]]

    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
            1.0
    
        """
    
        if len(data) == 0:
            raise ValueError("The list must have at least one element.")
    
        mean = mean(data)
        variance = 0.0
        for value in data:
            variance += (value - mean) ** 2
    
        standard_deviation = math.sqrt(variance)
        return standard_deviation

