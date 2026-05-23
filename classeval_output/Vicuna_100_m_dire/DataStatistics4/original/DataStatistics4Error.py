import math
class DataStatistics4: 


    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
    
        :param data1: The first set of data, list.
        :param data2: The second set of data, list.
        :return: The correlation coefficient, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998
    
        """
        if len(data1) != len(data2):
            raise ValueError("The two sets of data must have the same length.")
    
        mean_diff = (data1 + data2) / 2
        mean_diff = [math.sqrt(sum((x - mean_diff)**2 for x in data1))]
        mean_diff = [math.sqrt(sum((x - mean_diff)**2 for x in data2))]
        covariance = sum((x[0] - mean_diff) * (y[0] - mean_diff))
        covariance = sum((x[1] - mean_diff) * (y[1] - mean_diff))
        covariance = sum((x[2] - mean_diff) * (y[2] - mean_diff))
        covariance = sum((x[3] - mean_diff) * (y[3] - mean_diff))
        covariance = sum((x[4] - mean_diff) * (y[4] - mean_diff))
        covariance = sum((x[5] - mean_diff) * (y[5] - mean_diff))
        covariance = sum((x[6] - mean_diff) * (y[6] - mean_diff))
        covariance = sum((x[7] - mean_diff) * (y[7] - mean_diff))
        covariance = sum((x[8] - mean_diff) * (y[8] - mean_diff))
        covariance = sum((x[9] - mean_diff) * (y[9] - mean_diff))
        covariance = sum((x[10] - mean_diff) * (y[10] - mean_diff))
        covariance = sum((x[11] - mean_diff) * (y[11] - mean_diff))
        covariance = sum((x[12] - mean_diff) * (y[12] - mean_diff))
        covariance = sum((x[13] - mean_diff) * (y[13] - mean_diff))
        covariance = sum((x[14] - mean_diff) * (y[14] - mean_diff))
        covariance = sum((x[15] - mean_diff) * (y[15] - mean_diff))
        covariance = sum((x[16] - mean_diff) * (y[16] - mean_diff))
        covariance = sum((x[17] - mean_diff) * (y[17] - mean_diff))
        covariance = sum((x[18] - mean_diff) * (y[18] - mean_diff))
        covariance = sum((x[19] - mean_diff) * (y[19] - mean_diff))
        covariance = sum((x[20] - mean_diff) * (y[20] - mean_diff))
        covariance = sum((x[21] - mean_diff) * (y[21] - mean_diff))
        covariance = sum((x[22] - mean_diff) * (y[22] - mean_diff))
        covariance = sum((x[23] - mean_diff) * (y[23] - mean_diff))
        covariance = sum((x[24] - mean_diff) * (y[24] - mean_diff))
        covariance = sum((x[25] - mean_diff) * (y[25] - mean_diff))
        covariance = sum((x[26] - mean_diff) * (y[26] - mean_diff))
        covariance = sum((x[27] - mean_diff) * (y[27] - mean_diff))
        covariance = sum((x[28] - mean_diff) * (y[28] - mean_diff))
        covariance = sum((x[29] - mean_diff) * (y[29] - mean_diff))
        covariance = sum((x[30] - mean_diff) * (y[30] - mean_diff))
        covariance = sum((x[31] - mean_diff) * (y[31] - mean_diff))
        covariance = sum((x[32] - mean_diff) * (y[32] - mean_diff))
        covariance = sum((x[33] - mean_diff) * (y[33] - mean_diff))
        covariance = sum((x[34] - mean_diff) * (y[34] - mean_diff))
        covariance = sum((x[35] - mean_diff) * (y[35] - mean_diff))
        covariance = sum((x[36] - mean_diff) * (y[36] - mean_diff))
        covariance = sum((x[37] - mean_diff) * (y[37] - mean_diff))
        covariance = sum((x[38] - mean_diff) * (y[38] - mean_diff))
        covariance = sum((x[39] - mean_diff) * (y[39] - mean_diff))
        covariance = sum((x[40] - mean_diff) * (y[40] - mean_diff))
        covariance = sum((x[41] - mean_diff) * (y[41] - mean_diff))
        covariance = sum((x[42] - mean_diff) * (y[42] - mean_diff))
        covariance = sum((x[43] - mean_diff) * (y[43] - mean_diff))
        covariance = sum((x[44] - mean_diff) * (y[44] - mean_diff))
        covariance = sum((x[45] - mean_diff) * (y[45] - mean_diff))
        covariance = sum((x[46] - mean_diff) * (y[46] - mean_diff))
        covariance = sum((x[47] - mean_diff) * (y[47] - mean_diff))
        covariance = sum((x[48] - mean_diff) * (y[48] - mean_diff))
        covariance = sum((x[49] - mean_diff) * (y[49] - mean_diff))
        covariance = sum((x[50] - mean_diff) * (y[50] - mean_diff))
        covariance = sum((x[51] - mean_diff) * (y[5

    def skewness(data):
        """
        Calculate the skewness of a set of data.
    
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463
    
        """
        mu = sum(data) / len(data)
        sigma = 0
        for value in data:
            sigma += (value - mu) ** 3
        skewness = sigma / (mu ** 3)
        return skewness

    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
    
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007
    
        """
        # Get the mean and standard deviation of the data
        mean = sum(data) / len(data)
        std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    
        # Calculate the kurtosis
        kurtosis = (sum(((x - mean) ** 4 for x in data)) / (len(data) - 1)) - 3
    
        return kurtosis

    def pdf(data, mu, sigma):
        n = len(data)
        mean = sum(data) / n
        sigma_squared = sum([(x - mean)**2 for x in data]) / n
        mu_squared = mean**2 + sigma_squared
        mu_minus_squared = mean**2 - sigma_squared
        k = 1 / (sigma * sqrt(2*pi))
        pdf = [k / (sigma_squared * sqrt(2*pi)) * exp(-((x - mean)**2) / (2*sigma_squared)) for x in data]
        return pdf