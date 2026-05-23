
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
        # Initialize the list of slopes and y-coordinates
        slopes = []
        y_coords = []
        # Loop through each x-coordinate
        for i in range(len(x) - 1):
            # Calculate the slope
            slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            # Append the slope to the list of slopes
            slopes.append(slope)
            # Append the y-coordinate to the list of y-coordinates
            y_coords.append(y[i])
        # Loop through each x-coordinate in the interpolation point
        for i in range(len(x_interp)):
            # Initialize the variable to store the y-coordinate
            y_coord = 0
            # Calculate the y-coordinate
            for j in range(len(x) - 1):
                # Calculate the x-coordinate
                x_coord = x_interp[i]
                # Calculate the y-coordinate
                y_coord += slopes[j] * (x_coord - x[j])
            # Append the y-coordinate to the list of y-coordinates
            y_coords.append(y_coord)
        return y_coords

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
        # Initialize the list of slopes and y-coordinates
        slopes = []
        y_coords = []
        # Loop through each x-coordinate
        for i in range(len(x) - 1):
            # Calculate the slope
            slope = (z[i + 1] - z[i]) / (y[i + 1] - y[i])
            # Append the slope to the list of slopes
            slopes.append(slope)
            # Append the y-coordinate to the list of y-coordinates
            y_coords.append(z[i])
        # Loop through each x-coordinate in the interpolation point
        for i in range(len(x_interp)):
            # Initialize the variable to store the y-coordinate
            y_coord = 0
            # Calculate the y-coordinate
            for j in range(len(x) - 1):
                # Calculate the x-coordinate
                x_coord = x_interp[i]
                # Calculate the y-coordinate
                y_coord += slopes[j] * (x_coord - x[j])
            # Append the y-coordinate to the list of y-coordinates
            y_coords.append(y_coord)
        return y_coords