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
        data = sorted(data)
        if len(data) % 2 == 0:
            return (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
        else:
            return data[len(data) // 2]


    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        data = sorted(data)
        count = {}
        for i in data:
            count[i] = count.get(i, 0) + 1
        return [k for k, v in count.items() if v == max(count.values())]



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
        x = sorted(x)
        y = sorted(y)
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x * y)
        sum_xx = sum(x * x)
        sum_yy = sum(y * y)
        sum_xy_sq = sum(x * y * x)
        sum_xx_sq = sum(x * x * x)
        sum_yy_sq = sum(y * y * y)
        numerator = sum_xy - sum_x * sum_y / n
        denominator = math.sqrt((sum_xx - sum_x * sum_x / n) * (sum_yy - sum_y * sum_y / n))
        return numerator / denominator




    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
        data = sorted(data)
        return sum(data) / len(data)



    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        data = sorted(data)
        n = len(data)
        matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = data[i] * data[j]
        return matrix




    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        data = sorted(data)
        n = len(data)
        sum_data = sum(data)
        sum_sq_data = sum(x * x for x in data)
        return math.sqrt((sum_sq_data - (sum_data * sum_data) / n) / (n - 1))





    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
        data = sorted(data)
        n = len(data)
        mean = Statistics3.mean(data)
        sum_data = sum(data)
        sum_sq_data = sum(x * x for x in data)
        sum_sq_mean = sum(x * (x - mean) for x in data)
        return [(x - mean) / math.sqrt((sum_sq_data - (sum_data * sum_data) / n) / (n - 1)) for x in data]