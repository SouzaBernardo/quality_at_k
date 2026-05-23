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
        """
        n = len(data)
        sorted_data = sorted(data)
        if n % 2 == 0:
            return (sorted_data[n//2] + sorted_data[n//2 - 1]) / 2
        else:
            return sorted_data[n//2]

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        """
        mode_list = []
        max_count = 0
        for num in set(data):
            count = data.count(num)
            if count > max_count:
                mode_list = [num]
                max_count = count
            elif count == max_count:
                mode_list.append(num)
        return mode_list

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        """
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum([x[i]*y[i] for i in range(n)])
        sum_x2 = sum([x[i]**2 for i in range(n)])
        sum_y2 = sum([y[i]**2 for i in range(n)])
        numerator = n*sum_xy - sum_x*sum_y
        denominator = math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))
        if denominator == 0:
            return 0
        else:
            return numerator/denominator

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        """
        return sum(data)/len(data)

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        """
        n = len(data)
        corr_matrix = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                corr_matrix[i][j] = corr_matrix[j][i] = Statistics3.correlation(data[i], data[j])
        return corr_matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        """
        mean = Statistics3.mean(data)
        variance = sum([(x-mean)**2 for x in data])/len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        """
        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x-mean)/std_dev for x in data]

if __name__ == '__main__':
    import doctest
    doctest.testmod()