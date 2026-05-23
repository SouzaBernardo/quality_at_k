import numpy as np
class MetricsCalculator2: 
    def __init__(self):
        pass

    @staticmethod


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
        if isinstance(data, tuple):
            data = [data]
        mrr_list = []
        precision_list = []
        for item in data:
            actual_result, ground_truth_num = item
            reciprocal_rank = 0
            for i, result in enumerate(actual_result):
                if result == 1:
                    reciprocal_rank = 1 / (i + 1)
                    break
            mrr_list.append(reciprocal_rank)
            precision_list.append(sum(actual_result) / ground_truth_num)
        mrr = np.mean(mrr_list)
        return mrr, precision_list


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
        if isinstance(data, tuple):
            # If the input data is a tuple, calculate the average precision for that tuple
            actual_result, ground_truth_num = data
            precision = sum(actual_result) / ground_truth_num
            return precision
        elif isinstance(data, list):
            # If the input data is a list, calculate the average precision for each tuple and return the average recall
            precisions = []
            for item in data:
                actual_result, ground_truth_num = item
                precision = sum(actual_result) / ground_truth_num
                precisions.append(precision)
            average_recall = sum(precisions) / len(precisions)
            return average_recall, precisions