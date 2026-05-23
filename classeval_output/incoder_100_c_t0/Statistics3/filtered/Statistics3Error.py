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
            return (sorted_data[length//2] + sorted_data[length//2 - 1])/2

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
                modes.remove(sorted_data[i])
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
            sum += value**2
        return math.sqrt(sum/len(data))

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
        matrix = []
        for i in range(length):
            matrix.append([])
            for j in range(length):
                matrix[i].append(0)
        for i in range(length):
            for j in range(length):
                matrix[i][j] = data[i]*data[j]
        return matrix

    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
        length = len(data)
        sum = 0
        for i in range(length):
            sum += (data[i] - mean(data))**2
        return sum/length

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
            sum += value**2
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
        length = len(data)
        sum = 0
        for i in range(length):
            sum += (data[i] - mean(data))**2
        return sum/length

if __name__ == '__main__':
    import doctest
    doctest.testmod()