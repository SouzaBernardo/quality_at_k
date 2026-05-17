
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
        if len(x)!= len(y):
            raise ValueError("The length of x and y must be equal")
        if len(x) == 0:
            raise ValueError("The length of x must be greater than 0")
        if len(x) == 1:
            return x[0]
        if len(x) == 2:
            return x[0] + x[1] * (y[0] - x[0])
        if len(x) == 3:
            return x[0] + x[1] * (y[0] - x[0]) + x[2] * (y[1] - x[1])
        raise ValueError("The length of x must be greater than 0 and less than 3")


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
        if len(x) == 0:
            raise ValueError("The length of x must be greater than 0")
        if len(x) == 1:
            return x[0]
        if len(x) == 2:
            return x[0] + x[1] * (y[0] - x[0])
        if len(x) == 3:
            return x[0] + x[1] * (y[0] - x[0]) + x[2] * (y[1] - x[1])
        if len(x) == 4:
            return x[0] + x[1] * (y[0] - x[0]) + x[2] * (y[1] - x[1]) + x[3] * (y[2] - x[2])
        raise ValueError("The length of x must be greater than 0 and less than 3")


        """