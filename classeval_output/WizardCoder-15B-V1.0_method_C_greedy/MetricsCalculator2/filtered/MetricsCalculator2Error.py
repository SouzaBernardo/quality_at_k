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
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        if isinstance(data[0], list):
            total_mrr = 0
            total_precision = 0
            mrrs = []
            for d in data:
                mrr, precision = self._mrr(d)
                total_mrr += mrr
                total_precision += sum(precision)
                mrrs.append(mrr)
            return total_mrr / len(data), mrrs
        else:
            return self._mrr(data)