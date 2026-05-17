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
        return x_interp[0] * (1.0 - x[0]) + x_interp[1] * x[1] + x_interp[2] * x[2]


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
        if len(x)!= len(y):
            raise ValueError("The length of x and y must be equal")
        if len(x)!= len(z):
            raise ValueError("The length of z must be equal")
        if len(x)!= len(x_interp):
            raise ValueError("The length of x_interp must be equal")
        if len(y)!= len(y_interp):
            raise ValueError("The length of y_interp must be equal")
        if len(x)!= len(z):
            raise ValueError("The length of z must be equal")
        if len(x)!= len(x_interp):
            raise ValueError("The length of x_interp must be equal")

        if len(x) == 0:
            raise ValueError("The length of x must be greater than 0")
        if len(y) == 0:
            raise ValueError("The length of y must be greater than 0")
        if len(z) == 0:
            raise ValueError("The length of z must be greater than 0")
        if len(x_interp) == 0:
            raise ValueError("The length of x_interp must be greater than 0")
        if len(y_interp) == 0:
            raise ValueError("The length of y_interp must be greater than 0")
        if len(z) == 0:
            raise ValueError("The length of z must be greater than 0")

        if len(x) == 1:
            x_interp = [x_interp]
        if len(y) == 1:
            y_interp = [y_interp]
        if len(z) == 1:
            z = z[0]
        if len(x) == 1:
            x_interp = [x_interp]
        if len(y) == 1:
            y_interp = [y_interp]
        if len(z) == 1:
            z = z[0]

        if len(x) == 1:
            x_interp = [x_interp]
        if len(y) == 1:
            y_interp = [y_interp]
        if len(z) == 1:
            z = z[0]

        if len(x) == 1:
            x_interp = [x_interp]
        if len(y) == 1:
            y_interp = [y_interp]
        if len(z) == 1:
            z = z[0]

        if len(x) == 1:
            x_interp = [x_interp]
        if len(y) == 1:
            y_interp = [y_interp]
        if len(z) == 1:
            z = z[0]

        if len(x) == 1:
            x_interp = [x_interp]
        if len(y) == 1:
            y_interp = [y_interp]
     
        """