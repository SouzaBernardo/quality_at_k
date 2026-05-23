
class Interpolation: 
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
        """
        y_interp = []
        for xi in x_interp:
            if xi <= x[0]:
                y_interp.append(y[0])
            elif xi >= x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(len(x) - 1):
                    if xi >= x[i] and xi <= x[i + 1]:
                        yi = y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i])
                        y_interp.append(yi)
                        break
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
        interpolated_values = []
        for i in range(len(x_interp)):
            x1, x2 = None, None
            y1, y2 = None, None
            z1, z2 = None, None
    
            for j in range(len(x)):
                if x[j] <= x_interp[i]:
                    x1 = x[j]
                    y1 = y[j]
                    z1 = z[j]
                if x[j] >= x_interp[i]:
                    x2 = x[j]
                    y2 = y[j]
                    z2 = z[j]
                    break
    
            if x1 is not None and x2 is not None:
                for k in range(len(y)):
                    if y[k] <= y_interp[i]:
                        y1 = y[k]
                        z1 = z[k]
                    if y[k] >= y_interp[i]:
                        y2 = y[k]
                        z2 = z[k]
                        break
    
            if x1 is not None and x2 is not None and y1 is not None and y2 is not None:
                z_interp = z1 + (z2 - z1) * (x_interp[i] - x1) / (x2 - x1) + (z2 - z1) * (y_interp[i] - y1) / (y2 - y1)
                interpolated_values.append(z_interp)
    
        return interpolated_values
    