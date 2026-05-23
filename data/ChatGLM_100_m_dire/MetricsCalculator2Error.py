import numpy as np
class MetricsCalculator2: 
    def __init__(self):
        pass

    @staticmethod


    def mrr(self, data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr([([1,0,1,...],5),([1,0,...],6),([0,0,...],5]))
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
        if type(data) is tuple:
            recall_list = data
        elif type(data) is list:
            recall_list = list(data)
        else:
            raise ValueError("data must be a tuple, list or list of tuple")

        if len(recall_list) == 1:
            precision_list = recall_list[0]
        else:
            precision_list = []
            for i in range(len(recall_list)):
                precision_list.append(recall_list[i])

        return np.mean(precision_list), np.mean(recall_list)

    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
        if type(data) is list:
            recall_list = []
            precision_list = []
            for i, d in enumerate(data):
                if d == 1:
                    recall_list.append(np.mean(np.array(d, dtype=float)))
                else:
                    precision_list.append(np.mean(np.array(d, dtype=float)))
            return np.mean(recall_list), np.mean(precision_list)
        else:
            return np.mean(np.array(d, dtype=float)), np.mean(np.array(d, dtype=float))