import numpy as np
class MetricsCalculator2:  
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

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
        if len(data) == 1:
            return mrr_list[0], precision_list
        else:
            return sum(mrr_list) / len(mrr_list), precision_list


    @staticmethod
    def map(data):
        if isinstance(data, tuple):
            data = [data]
        map_list = []
        precision_list = []
        for item in data:
            actual_result, ground_truth_num = item
            average_precision = 0
            correct_count = 0
            for i, result in enumerate(actual_result):
                if result == 1:
                    correct_count += 1
                    average_precision += correct_count / (i + 1)
            average_precision /= ground_truth_num
            map_list.append(average_precision)
            precision_list.append(sum(actual_result) / ground_truth_num)
        if len(data) == 1:
            return map_list[0], precision_list
        else:
            return sum(map_list) / len(map_list), precision_list