Please complete the class Interpolation in the following code.

```python
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
        y_interp = []
        for xi in x_interp:
            if xi in x:
                y_interp.append(y[x.index(xi)])
            else:
                idx = 0
                while idx < len(x) and xi > x[idx]:
                    idx += 1
                if idx == 0:
                    y_interp.append(y[0])
                elif idx == len(x):
                    y_interp.append(y[-1])
                else:
                    y_interp.append(y[idx-1] + (y[idx] - y[idx-1]) * (xi - x[idx-1]) / (x[idx] - x[idx-1]))
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
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]

        """
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            if xi in x and yi in y:
                z_interp.append(z[y.index(yi)][x.index(xi)])
            else:
                idx_x = 0
                while idx_x < len(x) and xi > x[idx_x]:
                    idx_x += 1
                idx_y = 0
                while idx_y < len(y) and yi > y[idx_y]:
                    idx_y += 1
                if idx_x == 0:
                    x1 = x[0]
                    x2 = x[1]
                    z1 = z[idx_y][0]
                    z2 = z[idx_y][1]
                elif idx_x == len(x):
                    x1 = x[-2]
                    x2 = x[-1]
                    z1 = z[idx_y][-2]
                    z2 = z[idx_y][-1]
                else:
                    x1 = x[idx_x-1]
                    x2 = x[idx_x]
                    z1 = z[idx_y][idx_x-1]
                    z2 = z[idx_y][idx_x]
                if idx_y == 0:
                    y1 = y[0]
                    y2 = y[1]
                    z1 = z[0][idx_x]
                    z2 = z[1][idx_x]
                elif idx_y == len(y):
                    y1 = y[-2]
                    y2 = y[-1]
                    z1 = z[-2][idx_x]
                    z2 = z[-1][idx_x]
                else:
                    y1 = y[idx_y-1]
                    y2 = y[idx_y]
                    z1 = z[idx_y-1][idx_x]
                    z2 = z[idx_y][idx_x]
                z_interp.append(z1 + (z2 - z1) * (xi - x1) / (x2 - x1) + (z2 - z1) * (yi - y1) / (y2 - y1))
        return z_interp
```

This code completes the class Interpolation by implementing the interpolate_1d and interpolate_2d methods. The interpolate_1d method performs linear interpolation on one-dimensional data, while the interpolate_2d method performs linear interpolation on two-dimensional data. Both methods return the interpolated values based on the given input coordinates.