import math
class Statistics3:  
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """


    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            return sorted_data[length//2]
        else:
            return (sorted_data[length//2] + sorted_data[length//2 - 1])/2.0