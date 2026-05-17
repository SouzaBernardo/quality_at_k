import numpy as np
class MetricsCalculator2: 
    def __init__(self):
        pass

    @staticmethod


    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
        if isinstance(data, list):
            if len(data) == 1:
                return MetricsCalculator2.map(data[0])
            else:
                return MetricsCalculator2.map(data)
        elif isinstance(data, tuple):
            if len(data) == 2:
                return MetricsCalculator2.map(data)
            else:
                return MetricsCalculator2.map(data[0])
        else:
            return MetricsCalculator2.map(data)


    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
        if isinstance(data, list):
            data = np.array(data)
        if isinstance(data, tuple):
            data = np.array(data)
        if isinstance(data, np.ndarray):
            data = data.tolist()
        if len(data) == 0:
            return []
        if len(data) == 1:
            return [data[0]]
        if len(data) == 2:
            return [data[0], data[1]]
        if len(data) == 3:
            return [data[0], data[1], data[2]]
        if len(data) == 4:
            return [data[0], data[1], data[2], data[3]]
        if len(data) == 5:
            return [data[0], data[1], data[2], data[3], data[4]]
        if len(data) == 6:
            return [data[0], data[1], data[2], data[3], data[4], data[5]]
        return []


