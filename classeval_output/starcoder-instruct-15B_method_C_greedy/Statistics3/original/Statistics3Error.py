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
        data.sort()
        length = len(data)
        if length % 2 == 0:
            middle1 = data[length // 2]
            middle2 = data[length // 2 - 1]
            median = (middle1 + middle2) / 2
        else:
            median = data[length // 2]
        return median

    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        data.sort()
        count = 1
        max_count = 1
        mode_list = []

        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                mode_list.append(data[i - 1])
                max_count = max(max_count, count)
                count = 1

        mode_list.append(data[-1])
        max_count = max(max_count, count)

        return mode_list if max_count > 1 else [data[0]]

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
        numerator = sum([(x[i] - Statistics3.mean(x)) * (y[i] - Statistics3.mean(y)) for i in range(len(x))])
        denominator = math.sqrt(Statistics3.variance(x) * Statistics3.variance(y))
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
        n = len(data)
        corr_matrix = [[1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                corr_matrix[i][j] = Statistics3.correlation(data[i], data[j])

        return corr_matrix

    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        mean_val = Statistics3.mean(data)
        squared_diff = [math.pow(x - mean_val, 2) for x in data]
        variance = sum(squared_diff) / len(squared_diff)
        return math.sqrt(variance)

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
        std = Statistics3.standard_deviation(data)
        z_scores = [(x - mean) / std for x in data]
        return z_scores