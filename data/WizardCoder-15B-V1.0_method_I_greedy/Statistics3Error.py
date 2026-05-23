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
        """
        n = len(data)
        if n % 2 == 0:
            # if the list has even number of elements, return the average of the middle two values
            return (sorted(data)[n//2] + sorted(data)[n//2 - 1]) / 2
        else:
            # if the list has odd number of elements, return the middle value
            return sorted(data)[n//2]