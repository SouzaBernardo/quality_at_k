Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class MetricsCalculator2 in the following code.
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
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """


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

### Response:The class MetricsCalculator2 is already implemented. The only thing missing is the implementation of the `mrr` and `map` methods. Here's the updated implementation:

```python
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
            if isinstance(data[0], tuple):
                recalls = []
                precisions = []
                for d in data:
                    actual_result, ground_truth_num = d
                    rank = np.where(actual_result == 1)[0][0] + 1
                    recalls.append(1.0 / rank)
                    precisions.append(np.sum(actual_result[:rank]) / ground_truth_num)
                return np.mean(recalls), precisions
            else:
                actual_result, ground_truth_num = data
                rank = np.where(actual_result == 1)[0][0] + 1
                return 1.0 / rank, [np.sum(actual_result[:rank]) / ground_truth_num]
        else:
            raise ValueError("Input data must be a list or a tuple.")

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
        if isinstance(data, list):
            if isinstance(data[0], tuple):
                aps = []
                for d in data:
                    actual_result, ground_truth_num = d
                    precision, recall, _ = MetricsCalculator2._precision_recall_curve(actual_result, ground_truth_num)
                    ap = np.sum(precision * recall) / np.sum(recall)
                    aps.append(ap)
                return np.mean(aps), aps
            else:
                actual_result, ground_truth_num = data
                precision, recall, _ = MetricsCalculator2._precision_recall_curve(actual_result, ground_truth_num)
                ap = np.sum(precision * recall) / np.sum(recall)
                return ap, [ap]
        else:
            raise ValueError("Input data must be a list or a tuple.")

    @staticmethod
    def _precision_recall_curve(actual_result, ground_truth_num):
        """
        compute the precision, recall, and threshold of the input data.
        :param actual_result: the actual result of the input data.
        :param ground_truth_num: the total ground truth number of the input data.
        :return: precision, recall, and threshold.
        """
        precision, recall, threshold = [], [], []
        for i in range(1, len(actual_result) + 1):
            tp = np.sum(actual_result[:i])
            fp = i - tp
            fn = ground_truth_num - tp
            precision.append(tp / (tp + fp))
            recall.append(tp / (tp + fn))
            threshold.append(i / len(actual_result))