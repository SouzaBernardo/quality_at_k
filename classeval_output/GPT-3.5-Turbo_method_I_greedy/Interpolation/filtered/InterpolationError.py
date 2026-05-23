class Interpolation:  
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod


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
        for xi in x_interp:
            if xi in x:
                y_interp.append(y[x.index(xi)])
            else:
                x1 = max([x_val for x_val in x if x_val < xi])
                x2 = min([x_val for x_val in x if x_val > xi])
                y1 = y[x.index(x1)]
                y2 = y[x.index(x2)]
                y_interp.append(y1 + (y2 - y1) * (xi - x1) / (x2 - x1))
        return y_interp


    @staticmethod
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
        for xi, yi in zip(x_interp, y_interp):
            if xi in x and yi in y:
                z_interp.append(z[x.index(xi)][y.index(yi)])
            else:
                x1 = max([x_val for x_val in x if x_val < xi])
                x2 = min([x_val for x_val in x if x_val > xi])
                y1 = max([y_val for y_val in y if y_val < yi])
                y2 = min([y_val for y_val in y if y_val > yi])
                z11 = z[x.index(x1)][y.index(y1)]
                z12 = z[x.index(x1)][y.index(y2)]
                z21 = z[x.index(x2)][y.index(y1)]
                z22 = z[x.index(x2)][y.index(y2)]
                z_interp.append((z11 * (x2 - xi) * (y2 - yi) +
                                 z21 * (xi - x1) * (y2 - yi) +
                                 z12 * (x2 - xi) * (yi - y1) +
                                 z22 * (xi - x1) * (yi - y1)) / ((x2 - x1) * (y2 - y1)))
        return z_interp