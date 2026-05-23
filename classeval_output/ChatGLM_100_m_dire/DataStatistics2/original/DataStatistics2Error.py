import numpy as np
class DataStatistics2: 
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
        return self.data.sum()

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min()
        1
        """
        return self.data[0]

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_max()
        4
        """
        max_value = max(self.data)
        return max_value

    def get_variance(self):
        return self.get_std_deviation() / np.sqrt(self.get_sum() * self.get_max())





    def get_correlation(self, data1, data2):
        """
        Calculate correlation
        :param data1:list
        :param data2:list
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds1 = DataStatistics2([3, 4, 5, 6])
        >>> ds2.get_correlation(ds1)
        1.0
        """
        return np.correl(self.data, self.data)