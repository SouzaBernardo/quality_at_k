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
        # Calculate the median of the list using the built-in median function
        median = math. median(data)
        
        # Return the calculated median
        return median

    def mode(data):
        if len(data) == 1:
            return data[0]
        else:
            return data[0]

    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        """
        # Calculate the correlation matrix using the built-in correlation function
        corr = math.corr(x, y)
        
        # Return the calculated correlation matrix
        return corr



    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        """
        corr = [[math.corr(x, y) for x, y in zip(data, data)] for _ in range(len(data))]
        return [[math.corr(x, y) for x, y in zip(data, data)] for _ in range(len(data))]

    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        """
        # Calculate the mean of the list using the built-in mean function
        mean = math.mean(data)
        
        # Calculate the standard deviation of the list using the built-in standard_deviation function
        stddev = math.std(data)
        
        # Return the calculated standard deviation
        return stddev

    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        """
        # Calculate the z-score of the first element of the list using the built-in z_score function
        z_score = data[0]
        
        # Calculate the z-score of the rest of the elements of the list using the built-in z_score function
        for i in range(1, len(data)):
            z_score = math.zscore(data[i], z_score)
        
        # Return the calculated z-score
        return z_score