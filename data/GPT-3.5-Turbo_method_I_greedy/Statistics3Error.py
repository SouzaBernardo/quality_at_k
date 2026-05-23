import math
class Statistics3:  
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """



@staticmethod
    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            median1 = sorted_data[n // 2]
            median2 = sorted_data[n // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_data[n // 2]
        return median


    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]
        """
        counts = {}
        for num in data:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        max_count = max(counts.values())
        mode = [num for num, count in counts.items() if count == max_count]
        
        return mode
    

@staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0
        """
        correlation_coefficient = np.corrcoef(x, y)[0, 1]
        return correlation_coefficient


    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0
        """
        mean = sum(data) / len(data)
        return mean
    

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
        """
        correlation_matrix = []
        for i in range(len(data)):
            row = []
            for j in range(len(data)):
                correlation = Statistics3.correlation(data[i], data[j])
                row.append(correlation)
            correlation_matrix.append(row)
        return correlation_matrix
    

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0
        """
        mean = Statistics3.mean(data)
        squared_diff = [(x - mean) ** 2 for x in data]
        variance = sum(squared_diff) / len(data)
        standard_deviation = math.sqrt(variance)
        return standard_deviation
    

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]
        """
        mean = Statistics3.mean(data)
        standard_deviation = Statistics3.standard_deviation(data)
        z_scores = [(x - mean) / standard_deviation for x in data]
        return z_scores