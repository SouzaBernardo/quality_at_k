import numpy as np
class MetricsCalculator2: 
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
                    if data[i][0] == data[i][1]:
                        recall += 1
                        precision.append(1)
                    else:
                        precision.append(0)
                return recall / len(data), precision
        else:
            if data[0] == data[1]:
                return 1, [1]
            else:
                return 0, [0]


@staticmethod
    def map(data):
