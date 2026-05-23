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
        """
        return [(y[i] + (y[i+1] - y[i]) * (x_interp[j] - x[i]) / (x[i+1] - x[i])) for i in range(len(x)-1) for j in range(len(x_interp))]

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
        """
        return [[(z[i][j] + (z[i+1][j] - z[i][j]) * (x_interp[k] - x[i]) / (x[i+1] - x[i]) + (z[i][j+1] - z[i][j]) * (y_interp[l] - y[j]) / (y[j+1] - y[j])) for j in range(len(y)-1) for k in range(len(x_interp))] for i in range(len(x)-1)]


I hope this helps!