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
            recall = []
            for i in range(len(data)):
                recall.append(1.0 / np.amax(data[i][1]) * np.amax(data[i][0]) / np.amax(data[i][0]) + 1)
            return recall, np.array([p for i in range(len(data)) for p in data[i][2]])
        else:
            return 1.0 / np.amax(data[1]) * np.amax(data[0]) / np.amax(data[0]) + 1, data[2]

    def map(self, data):
        """
        Compute the Mean Average Precision (MAP) of the input data.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: the MAP of the input data.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        0.41666666666666663
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, 0.41666666666666663
        """
        if isinstance(data, list):
            if len(data) == 1:
                return np.mean([precision for _, precision in data])
            else:
                return np.mean([precision for _, precision in data])
        else:
            return np.mean([precision for _, precision in data])