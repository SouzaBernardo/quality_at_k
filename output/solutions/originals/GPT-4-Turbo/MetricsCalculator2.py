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
        if isinstance(data[0], list):
            mrrs = [MetricsCalculator2.mrr(d) for d in data]
            return np.mean(mrrs), mrrs
        else:
            ranks = [i for i, x in enumerate(data[0], 1) if x]
            return 1.0 / ranks[0] if ranks else 0.0

    @staticmethod
    def map(data):
        if isinstance(data[0], list):
            maps = [MetricsCalculator2.map(d) for d in data]
            return np.mean(maps), maps
        else:
            correct = 0
            total = 0
            scores = []
            for i, x in enumerate(data[0], 1):
                if x:
                    correct += 1
                    scores.append(correct / i)
            return np.mean(scores) if scores else 0.0
```
This code completes the MetricsCalculator2 class by implementing the mrr and map methods. The mrr method calculates the Mean Reciprocal Rank (MRR) of the input data, and the map method calculates the Mean Average Precision (MAP) of the input data. Both methods can handle a single list of data or a list of lists of data.