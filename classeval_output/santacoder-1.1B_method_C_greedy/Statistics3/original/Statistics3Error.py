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
        pass


    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        pass


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
        if len(x)!= len(y):
            raise ValueError("The given lists must have the same length.")
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x * y)
        sum_x2 = sum(x ** 2)
        sum_y2 = sum(y ** 2)
        sum_x_y = sum(x * y)
        sum_x_y2 = sum(x * y ** 2)
        sum_x_y_sum_x = sum(x * y)
        sum_x_y_sum_y = sum(x * y)
        sum_x_y_sum_xy = sum(x * y * x)
        sum_x_y_sum_x2 = sum(x * y ** 2)
        sum_x_y_sum_y2 = sum(x * y ** 2)
        sum_x_y_sum_x_y = sum(x * y * x)
        sum_x_y_sum_x_y2 = sum(x * y ** 2 * x)
        sum_x_y_sum_x_y_sum_x = sum(x * y * x)
        sum_x_y_sum_x_y_sum_y = sum(x * y * x)
        sum_x_y_sum_x_y_sum_xy = sum(x * y * x * x)
        sum_x_y_sum_x_y_sum_x2 = sum(x * y ** 2 * x)
        sum_x_y_sum_x_y_sum_y2 = sum(x * y ** 2 * x)
        sum_x_y_sum_x_y_sum_x_y = sum(x * y * x * x)
        sum_x_y_sum_x_y_sum_x_y2 = sum(x * y ** 2 * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x = sum(x * y * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_y = sum(x * y * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_xy = sum(x * y * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x2 = sum(x * y ** 2 * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_y2 = sum(x * y ** 2 * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y = sum(x * y * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y2 = sum(x * y ** 2 * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x = sum(x * y * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_y = sum(x * y * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_xy = sum(x * y * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x2 = sum(x * y ** 2 * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_y2 = sum(x * y ** 2 * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y = sum(x * y * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y2 = sum(x * y ** 2 * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x = sum(x * y * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_y = sum(x * y * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_xy = sum(x * y * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x2 = sum(x * y ** 2 * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_y2 = sum(x * y ** 2 * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y = sum(x * y * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y2 = sum(x * y ** 2 * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x = sum(x * y * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_y = sum(x * y * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_xy = sum(x * y * x * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x2 = sum(x * y ** 2 * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_y2 = sum(x * y ** 2 * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y = sum(x * y * x * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y2 = sum(x * y ** 2 * x * x * x * x * x * x * x)
        sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_sum_x_y_

    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
        pass


    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        pass


    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        pass


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
        z_score = [x - mean for x in data]
        z_score = [x / std for x in z_score]
        return z_score
