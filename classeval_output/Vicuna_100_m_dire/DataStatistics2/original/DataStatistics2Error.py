import numpy as np
class DataStatistics2: 
    def __init__(self, data):
        """
        Initialize Data List
        :param data:list
        """
        self.data = np.array(data)



    def get_sum(self):
        return np.sum(self.data)

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min()
        1
        """
        min_val = np.min(self.data)
        return min_val

    def get_max(self):
        max_val = np.amax(self.data)
        return max_val

    def get_variance(self):
        sum_of_squares = np.sum(self.data**2)
        n = len(self.data)
        variance = (sum_of_squares / n) - (1.0 / n)
        return variance

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """
        x = self.data
        return np.sqrt(np.mean((x - np.mean(x))**2))

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
        mean = np.mean(self.data)
        return np.corrcoef(self.data, mean)[0,1]