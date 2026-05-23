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
        
        if isinstance(data, list):
            if len(data) == 0:
                return 0, []
            else:
                recall = 0
                precision = []
                for i in range(len(data)):
                    if data[i][0].count(1) == 0:
                        precision.append(0)
                    else:
                        precision.append(data[i][0].count(1) / len(data[i][0]))
                    recall += data[i][0].count(1) / data[i][1]
                return recall / len(data), precision
        else:
            if data[0].count(1) == 0:
                return 0
            else:
                return data[0].count(1) / data[1]


@staticmethod
    def map(data):
