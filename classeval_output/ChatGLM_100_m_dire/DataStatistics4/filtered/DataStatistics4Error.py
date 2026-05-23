import math
class DataStatistics4: 




    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list or tuple.
        :return: The skewness, float.
        """
        n = len(data)
        mu = data[0]
        sigma = data[1]
         skewness = 0.0
        for i in range(n):
            if (data[i] - mu) ** 2 < (sigma ** 2):
                 skewness += 1.0
        return skewness