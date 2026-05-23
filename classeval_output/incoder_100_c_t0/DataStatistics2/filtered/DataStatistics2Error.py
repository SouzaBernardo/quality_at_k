class DataStatistics2:  
    """
    This is a class for performing data statistics, supporting to get the sum, minimum, maximum, variance, standard deviation, and correlation of a given dataset.
    """

    def __init__(self, data):
        """
        Initialize Data List
        :param data:list
        """
        self.data = np.array(data)


    def get_sum(self):
        """
        Calculate the sum of data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_sum()
        10
        """
        sum = 0
        for item in self.data:
            sum += item
        return sum

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min()
        1
        """
        min = min(self.data)
        return min

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_max()
        4
        """
        max = max(self.data)
        return max

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """
        sum = 0
        sum2 = 0
        for item in self.data:
            sum += item
            sum2 += (item - sum)**2
        return sum/len(self.data)-sum2/len(self.data)**2

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """
        sum = 0
        sum2 = 0
        for item in self.data:
            sum += item
            sum2 += (item - sum)**2
        return sum/len(self.data)**0.5-sum2/len(self.data)**0.5

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """
        sum = 0
        sum2 = 0
        for item in self.data:
            sum += item
            sum2 += (item - sum)**2
        return sum/len(self.data)**0.5-sum2/len(self.data)**0.5

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """
        sum = 0
        sum2 = 0
        for item in self.data:
            sum += item
            sum2 += (item - sum)**2
        return sum/len(self.data)**0.5-sum2/len(self.data)**0.5

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
        sum = 0
        sum2 = 0
        sum3 = 0
        for item in self.data:
            sum += item
            sum2 += (item - sum)**2
            sum3 += (item - sum2)**2
        return sum/len(self.data)**0.5-(sum2/len(self.data)**0.5)*(sum3/len(self.data)**0.5)

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
        sum = 0
        sum2 = 0
        sum3 = 0
        for item in self.data:
            sum += item
            sum2 += (item - sum)**2
            sum3 += (item - sum2)**2
        return sum/len(self.data)**0.5-(sum2/len(self.data)**0.5)*(sum3/len(self.data)**0.5)