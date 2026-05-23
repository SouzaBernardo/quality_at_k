import numpy as np
class MetricsCalculator2: 
    def __init__(self):
        pass

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
        0.416666666666666663, [0.416666666666666663]
        0.33333333333333333, [0.416666666666666663, 0.25]
        """
        actual_result, ground_truth_num = data
        if isinstance(actual_result, list):
            precision_list = []
            for item in actual_result:
                if item == 1:
                    precision_list.append(actual_result.index(item) / ground_truth_num)
            return np.mean(precision_list), precision_list
        else:
            if actual_result == 1:
                return actual_result.index(1) / ground_truth_num, [actual_result.index(1) / ground_truth_num]
            else:
                return 0, [0]