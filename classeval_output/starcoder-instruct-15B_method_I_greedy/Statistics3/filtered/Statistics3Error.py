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
        data.sort()
        length = len(data)
        if length % 2 == 0:
            middle1 = data[length // 2]
            middle2 = data[length // 2 - 1]
            median_value = (middle1 + middle2) / 2
        else:
            median_value = data[length // 2]
        return median_value

    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        count = {}
        for item in data:
            count[item] = count.get(item, 0) + 1
        mode_list = []
        for item, freq in count.items():
            if freq == max(count.values()):
                mode_list.append(item)
        return mode_list

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
        x_mean = sum(x) / len(x)
        y_mean = sum(y) / len(y)
        numerator = sum([(a - x_mean) * (b - y_mean) for a, b in zip(x, y)])
        denominator = math.sqrt(sum([(a - x_mean) ** 2 for a in x]) * sum([(b - y_mean) ** 2 for b in y]))
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
        matrix = [[1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = Statistics3.correlation(data[i], data[j])
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
        mean_value = Statistics3.mean(data)
        squared_diff = [math.pow(x - mean_value, 2) for x in data]
        variance = sum(squared_diff) / len(squared_diff)
        return math.sqrt(variance)