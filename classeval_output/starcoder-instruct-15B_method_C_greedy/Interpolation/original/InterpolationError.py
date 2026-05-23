
class Interpolation: 
    def __init__(self):
        pass

    @staticmethod


    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list or numpy array.
        :param y: The y-coordinate of the data point, list or numpy array.
        :param x_interp: The x-coordinate of the interpolation point, list or numpy array.
        :return: The y-coordinate of the interpolation point, list or numpy array.
        >>> interpolation = Interpolation()
        >>> x = [1, 2, 3]
        >>> y = [1, 2, 3]
        >>> x_interp = [1.5, 2.5]
        >>> interpolation.interpolate_1d(x, y, x_interp)
        [1.5, 2.5]

        """
        if isinstance(x, list):
            x = np.array(x)
        if isinstance(y, list):
            y = np.array(y)
        if isinstance(x_interp, list):
            x_interp = np.array(x_interp)

        y_interp = np.interp(x_interp, x, y)

        return y_interp.tolist()

    def interpolate_2d(x, y, z, x_interp, y_interp):
        z_interp = []
        for i in range(len(x_interp)):
            z_interp.append(np.interp(y_interp[i], y, z[i]))
        return z_interp