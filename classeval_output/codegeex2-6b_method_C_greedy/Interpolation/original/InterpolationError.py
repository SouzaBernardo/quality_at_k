
class Interpolation: 
    def __init__(self):
        pass

    @staticmethod


    @staticmethod
    def interpolate_1d(x, y, x_interp):
        

        x_interp_index = [i for i, x_interp_i in enumerate(x_interp) if x_interp_i in x]
        x_interp_index_1 = [i for i, x_interp_i in enumerate(x_interp) if x_interp_i not in x]
        x_interp_index_2 = [i for i, x_interp_i in enumerate(x_interp) if x_interp_i not in x]
        y_interp_index = [i for i, y_interp_i in enumerate(y) if y_interp_i in y]
        y_interp_index_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y]
        y_interp_index_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y]

        y_interp_index_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index]
        y_interp_index_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index]

        y_interp_index_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2]
        y_interp_index_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2]

        y_interp_index_1_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1]
        y_interp_index_1_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1]

        y_interp_index_1_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_2]
        y_interp_index_1_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_2]

        y_interp_index_2_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_1]
        y_interp_index_2_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_1]

        y_interp_index_2_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_2]
        y_interp_index_2_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_2]

        y_interp_index_1_1_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_1]
        y_interp_index_1_1_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_1]

        y_interp_index_1_1_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_1_2]
        y_interp_index_1_1_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_1_2]

        y_interp_index_1_2_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_2_1]
        y_interp_index_1_2_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_2_1]

        y_interp_index_1_2_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_2_2]
        y_interp_index_1_2_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_1_2_2]

        y_interp_index_2_1_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_1_1]
        y_interp_index_2_1_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_1_1]

        y_interp_index_2_1_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_1_2]
        y_interp_index_2_1_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_1_2]

        y_interp_index_2_2_1_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_2_1]
        y_interp_index_2_2_1_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_2_1]

        y_interp_index_2_2_2_1 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_2_2]
        y_interp_index_2_2_2_2 = [i for i, y_interp_i in enumerate(y) if y_interp_i not in y_interp_index_2_2_2]

        y_interp_index_1_1


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
