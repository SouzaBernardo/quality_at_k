```python
from scipy.interpolate import interp1d, interp2d

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
        f = interp1d(x, y)
        return f(x_interp)

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
        f = interp2d(x, y, z)
        return f(x_interp, y_interp)
```
This code uses the `interp1d` and `interp2d` functions from the `scipy.interpolate` module to perform one-dimensional and two-dimensional linear interpolation, respectively. The `interp1d` function creates a function that can be used to interpolate a 1-D function, and the `interp2d` function creates a function that can be used to interpolate a 2-D function.