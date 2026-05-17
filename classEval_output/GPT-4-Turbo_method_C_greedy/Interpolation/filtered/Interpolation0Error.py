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
            if xi in x:
                y_interp.append(y[x.index(xi)])
            else:
                i = 0
                while xi > x[i]:
                    i += 1
                x1, x2 = x[i - 1], x[i]
                y1, y2 = y[i - 1], y[i]
                yi = y1 + ((y2 - y1) / (x2 - x1)) * (xi - x1)
                y_interp.append(yi)
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
        """
        # Create a grid of points
        points = np.array([x, y]).T
        values = np.array(z)
    
        # Interpolate the z-values
        z_interp = griddata(points, values, (x_interp, y_interp), method='linear')
    
        return z_interp.tolist()