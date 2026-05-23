import numpy as np
class MetricsCalculator2:  
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod




    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
        if isinstance(data, list):
            if isinstance(data[0], tuple):
                recalls = []
                precisions = []
                for d in data:
                    actual_result, ground_truth_num = d
                    precision, recall = MetricsCalculator2.calculate_precision_recall(actual_result, ground_truth_num)
                    recalls.append(recall)
                    precisions.append(precision)
                return np.mean(recalls), precisions
            else:
                actual_result, ground_truth_num = data
                precision, recall = MetricsCalculator2.calculate_precision_recall(actual_result, ground_truth_num)
                return recall, [precision]
        else:
            raise ValueError("Input data must be a list or a list of tuple")