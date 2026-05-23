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
        if isinstance(data[0], list):
            mrr_list = [MetricsCalculator2.mrr(d)[0] for d in data]
            return np.mean(mrr_list), mrr_list
        else:
            ranks = [i+1 for i, x in enumerate(data[0]) if x == 1]
            if ranks:
                return 1.0 / min(ranks), [1.0 / rank for rank in ranks]
            else:
                return 0.0, [0.0]

    @staticmethod
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
        if not isinstance(data[0], list):
            data = [data]

        ap_list = []
        for actual, total in data:
            temp = [x for x in zip(actual, range(1, len(actual) + 1)) if x[0] == 1]
            if len(temp) == 0:
                ap_list.append(0)
                continue
            ap = np.mean([x[1] / (i + 1) for i, x in enumerate(temp)])
            ap_list.append(ap)

        return np.mean(ap_list), ap_list

