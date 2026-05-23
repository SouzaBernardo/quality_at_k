class Interpolation:  
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod


    @staticmethod
    def interpolate_1d(x, y, x_interp):
        

        x_interp_index = [i for i, x_interp_i in enumerate(x_interp) if x_interp_i in x]
        x_interp_index_1 = [i for i, x_interp_i in enumerate(x_interp) if x_interp_i not in x]
        y_interp = []
        for i in x_interp_index:
            y_interp.append(y[i])
        for i in x_interp_index_1:
            y_interp.append(y[i - 1] + (y[i] - y[i - 1]) * (x_interp[i] - x[i - 1]) / (x[i] - x[i - 1]))
        return y_interp


    def interpolate_2d(x, y, z, x_interp, y_interp):


@staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        ”“”
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

        ”“”