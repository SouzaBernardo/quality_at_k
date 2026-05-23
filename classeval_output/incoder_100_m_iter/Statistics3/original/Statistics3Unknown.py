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
        sorted_data = sorted(data)
        length = len(sorted_data)
        modes = []
        for i in range(length):
            if sorted_data[i] not in modes:
                modes.append(sorted_data[i])
            else:
                index = modes.index(sorted_data[i])
                if index == length-1:
                    modes.remove(sorted_data[i])
                else:
                    modes[index] = sorted_data[i]
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
        length = len(x)
        sum = 0
        for i in range(length):
            sum += (x[i] - y[i])**2
        return sum/length

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
        for value in data:
            sum += value
        return sum/len(data)

    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        length = len(data)
        correlation_matrix = [[0 for x in range(length)] for y in range(length)]
        for i in range(length):
            for j in range(length):
                correlation_matrix[i][j] = Statistics3.correlation(data[i], data[j])
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
        sum = 0
        for value in data:
            sum += (value - Statistics3.mean(data))**2
        return math.sqrt(sum/len(data))

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
        length = len(data)
        z_score = [0 for x in range(length)]
        for i in range(length):
            z_score[i] = (data[i] - mean)/standard_deviation
        return z_score
