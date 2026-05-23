
class Interpolation:  
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod


    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]
    
        """
        y_interp = []
        for x_i in x_interp:
            if x_i < x[0]:
                y_interp.append(y[0])
            elif x_i > x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(len(x) - 1):
                    if x_i >= x[i] and x_i <= x[i + 1]:
                        y_interp.append(y[i] + (x_i - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i]))
        return y_interp

    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]
        """
        z_interp = []
        for x_i, y_i in zip(x_interp, y_interp):
            if x_i < x[0] or x_i > x[-1] or y_i < y[0] or y_i > y[-1]:
                z_interp.append(None)
            else:
                for i in range(len(x) - 1):
                    if x_i >= x[i] and x_i <= x[i + 1]:
                        for j in range(len(y) - 1):
                            if y_i >= y[j] and y_i <= y[j + 1]:
                                z_interp.append(z[i][j] + (x_i - x[i]) * (z[i + 1][j] - z[i][j]) / (x[i + 1] - x[i]) + (y_i - y[j]) * (z[i][j + 1] - z[i][j]) / (y[j + 1] - y[j]))
        return z_interp