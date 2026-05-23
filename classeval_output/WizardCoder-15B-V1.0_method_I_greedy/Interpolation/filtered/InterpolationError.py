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
        y_interp = []
        for x_i in x_interp:
            i = 0
            while x[i] < x_i:
                i += 1
            y_interp.append((y[i+1] - y[i]) / (x[i+1] - x[i]) * (x_i - x[i]) + y[i])
        return y_interp