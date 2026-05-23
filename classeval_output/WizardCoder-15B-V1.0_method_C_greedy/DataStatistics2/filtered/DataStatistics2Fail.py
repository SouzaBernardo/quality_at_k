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
        return np.sum(self.data)

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        """
        return np.min(self.data)

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        """
        return np.max(self.data)

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        """
        mean = np.mean(self.data)
        variance = np.sum((self.data - mean) ** 2) / len(self.data)
        return round(variance, 2)
    

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        """
        return round(np.std(self.data, ddof=1), 2)

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        """
        if len(self.data) < 2:
            return 0.0
        else:
            mean = np.mean(self.data)
            std_dev = np.std(self.data)
            if std_dev == 0:
                return 0.0
            else:
                return np.corrcoef(self.data, mean)[0][1]