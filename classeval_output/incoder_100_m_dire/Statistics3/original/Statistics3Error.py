import math
class Statistics3: 


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
        length = len(sorted_data)
        if length % 2 == 0:
            return sorted_data[length//2]
        else:
            return (sorted_data[length//2] + sorted_data[length//2 - 1])/2.0


    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        modes = []
        mode_count = {}
        for value in data:
            if value in mode_count:
                mode_count[value] += 1
            else:
                mode_count[value] = 1
                modes.append(value)
        return modes


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
        import numpy as np
        corr = np.corrcoef(x, y)[0][1]
        return corr


    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
        sum = 0
        for x in data:
            sum += x
        return sum / len(data)


    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        correlation_matrix = [[0 for x in range(len(data))] for y in range(len(data))]
        for i in range(len(data)):
            for j in range(len(data)):
                correlation_matrix[i][j] = data[i] * data[j]
        return correlation_matrix


    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        mean = statistics3.mean(data)
        variance = statistics3.variance(data)
        standard_deviation = math.sqrt(variance)
        return standard_deviation


    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
        mean = statistics3.mean(data)
        variance = statistics3.standard_deviation(data)
        standard_deviation = math.sqrt(variance)
        z_score = (data - mean) / standard_deviation
        return z_score
