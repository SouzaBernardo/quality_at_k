import math
class Statistics3: 




    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        """
        if len(data) == 0:
            return []
        counts = {}
        for item in data:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        max_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == max_count]
        return modes



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
        """
        n = len(data)
        correlation_matrix = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                x = data[i]
                y = data[j]
                mean_x = sum(x) / len(x)
                mean_y = sum(y) / len(y)
                std_x = math.sqrt(sum([(x[i] - mean_x)**2 for i in range(len(x))]) / len(x))
                std_y = math.sqrt(sum([(y[i] - mean_y)**2 for i in range(len(y))]) / len(y))
                cov = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))]) / len(x)
                correlation_matrix[i][j] = cov / (std_x * std_y)
                correlation_matrix[j][i] = correlation_matrix[i][j]
        return correlation_matrix

    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        return math.sqrt(variance)

    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        """
        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores
    