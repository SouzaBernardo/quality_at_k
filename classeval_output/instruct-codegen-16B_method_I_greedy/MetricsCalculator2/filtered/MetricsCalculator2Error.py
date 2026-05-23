import numpy as np
class MetricsCalculator2:  
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod


    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5). In each tuple (actual result,ground truth num),ground truth num is the total ground num.
        eg. ([1,0,...],5),
            or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
            average recall on all list. The second return value is a list of precision for each input.
        """
        if isinstance(data, list):
            return np.mean([MetricsCalculator2.mrr(x) for x in data])
        else:
            data = list(data)
            tot_correct = sum([1 for x in data if x[0] == 1])
            return tot_correct/data[1]

    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        if isinstance(data, list):
            return np.mean([MetricsCalculator2.map(x) for x in data])
        else:
            data = list(data)
            tot_correct = sum([1 for x in data if x[0] == 1])
            return tot_correct/data[1]