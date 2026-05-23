class DataStatistics:  
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """


    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        sum = 0
        for x in data:
            sum += x
        return sum / len(data)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            return sorted_data[length / 2]
        else:
            return (sorted_data[length / 2] + sorted_data[length / 2 - 1]) / 2

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            return sorted_data[length / 2]
        else:
            return sorted_data[length / 2]

<|/ file |>
