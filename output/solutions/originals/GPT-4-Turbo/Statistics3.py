```python
import math
import numpy as np
from scipy import stats
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        data.sort()
        n = len(data)
        m = n - 1
        return (data[m//2] + data[(m+1)//2]) / 2.0

    @staticmethod
    def mode(data):
        c = Counter(data)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    @staticmethod
    def correlation(x, y):
        return np.corrcoef(x, y)[0, 1]

    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        return np.corrcoef(data)

    @staticmethod
    def standard_deviation(data):
        mean = Statistics3.mean(data)
        variance = sum((xi - mean) ** 2 for xi in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        mean = Statistics3.mean(data)
        stdev = Statistics3.standard_deviation(data)
        return [(x - mean) / stdev for x in data]
```