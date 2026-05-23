class Interpolation: 
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
        for xi in x_interp:
            if xi < min(x) or xi > max(x):
                y_interp.append(None)
            else:
                i = 0
                while xi > x[i]:
                    i += 1
                y_interp.append((y[i] - y[i - 1]) / (x[i] - x[i - 1]) * (xi - x[i - 1]) + y[i - 1])
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
        """
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            # Find the four surrounding data points
            x_min = min(x, key=lambda x_val: abs(x_val - xi))
            x_max = max(x, key=lambda x_val: abs(x_val - xi))
            y_min = min(y, key=lambda y_val: abs(y_val - yi))
            y_max = max(y, key=lambda y_val: abs(y_val - yi))
            # Calculate the weights for each surrounding data point
            wx = (xi - x_min) / (x_max - x_min)
            wy = (yi - y_min) / (y_max - y_min)
            # Calculate the interpolated z-coordinate
            z_interp.append((1 - wx) * (1 - wy) * z[x.index(x_min)][y.index(y_min)] +
                            wx * (1 - wy) * z[x.index(x_max)][y.index(y_min)] +
                            (1 - wx) * wy * z[x.index(x_min)][y.index(y_max)] +
                            wx * wy * z[x.index(x_max)][y.index(y_max)])
        return z_interp