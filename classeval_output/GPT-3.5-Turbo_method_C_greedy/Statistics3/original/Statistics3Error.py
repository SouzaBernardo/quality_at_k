import math
class Statistics3: 


    @staticmethod
    def median(data):
        """
        Calculates the median of the given list.
        :param data: The given list, list.
        :return: The median of the given list, float.
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            median_index = n // 2
            median = (sorted_data[median_index - 1] + sorted_data[median_index]) / 2
        else:
            median_index = n // 2
            median = sorted_data[median_index]
        return median
    

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        """
        return statistics.mode(data)
    

    @staticmethod
    def correlation(x, y):
        """
        Calculates the correlation between two lists.
        :param x: The first list, list.
        :param y: The second list, list.
        :return: The correlation between the two lists, float.
        """
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x)) * math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
        correlation = numerator / denominator
        return correlation
    

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        """
        return sum(data) / len(data)
    

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        """
        n = len(data)
        matrix = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = Statistics3.correlation(data[i], data[j])
        
        return matrix
    

    @staticmethod
    def standard_deviation(data):
        """
        Calculates the standard deviation of the given list.
        :param data: The given list, list.
        :return: The standard deviation of the given list, float.
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        standard_deviation = math.sqrt(variance)
        return standard_deviation
    

    @staticmethod
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
    