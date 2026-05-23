import numpy as np
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
        """
        return np.sum(self.data)



    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        """
        return np.max(self.data)