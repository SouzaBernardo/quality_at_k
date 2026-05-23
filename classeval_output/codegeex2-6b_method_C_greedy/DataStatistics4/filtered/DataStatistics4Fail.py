import math
class DataStatistics4: 


    @staticmethod
    def correlation_coefficient(data1, data2):
        

        n = len(data1)
        if n != len(data2):
            raise ValueError("The two data sets must have the same number of elements.")
        if n < 2:
            raise ValueError("The two data sets must have at least two elements.")
        if n == 2:
            return (data1[0] - data2[0]) / math.sqrt(data1[0] ** 2 + data2[0] ** 2)
        sum1 = sum(data1)
        sum2 = sum(data2)
        sum_product = 0
        sum_sqr1 = 0
        sum_sqr2 = 0
        for i in range(n):
            sum_product += data1[i] * data2[i]
            sum_sqr1 += data1[i] ** 2
            sum_sqr2 += data2[i] ** 2
        numerator = n * sum_product - sum1 * sum2
        denominator = math.sqrt(n * sum_sqr1 - sum1 ** 2) * math.sqrt(n * sum_sqr2 - sum2 ** 2)
        return numerator / denominator


@staticmethod
    def skewness(data):
        

        n = len(data)
        mean = sum(data) / n
        std = (sum(x * x for x in data) / n - mean ** 2) ** 0.5
        skew = sum((x - mean) ** 3 for x in data) / (n * std ** 3)
        return skew


@staticmethod
    def kurtosis(data):


@staticmethod
    def pdf(data, mu, sigma):