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
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr([([1,0,1,...],5),([1,0,...],6),([0,0,...],5)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
        if type(data) is list:
            recall_list = []
            for i, d in enumerate(data):
                if d == 1:
                    recall_list.append(1.0)
                else:
                    precision_list = []
                    for j, t in enumerate(d):
                        if t == 1:
                            precision_list.append(1.0)
                        else:
                            precision_list.append(0.5)
                    recall_list.append(np.mean(precision_list))
            return np.mean(recall_list), precision_list
        else:
            return data[0], data[1]

    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
             ([1,0,...],5),
            or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5].
            1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map([([1,0,1,...],5),([1,0,...],6),([0,0,...],5)])
        0.41666666666666663, [0.41666666666666663]
        """
        if type(data) is list:
            recall_list = []
            for i, d in enumerate(data):
                if d == 1:
                    recall_list.append(1.0)
                else:
                    precision_list = []
                    for j, t in enumerate(d):
                        if t == 1:
                            precision_list.append(1.0)
                        else:
                            precision_list.append(0.5)
                    recall_list.append(np.mean(precision_list))
            return np.mean(recall_list), precision_list
        else:
            return data[0], data[1]