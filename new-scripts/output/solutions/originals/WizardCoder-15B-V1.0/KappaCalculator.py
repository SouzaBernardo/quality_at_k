Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class KappaCalculator in the following code.
import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """


    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """

### Response:The class KappaCalculator is already implemented and complete. The only thing that needs to be added is the implementation of the static methods kappa and fleiss_kappa. 

Here's the updated implementation of the class:

```python
import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """

    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        """
        n = len(testData)
        p = np.sum(testData, axis=0) / n
        P = np.sum(p) / k
        Pbar = np.sum(p ** 2) / k
        PbarE = P * (1 - P)
        kappa = (P - Pbar) / (1 - PbarE)
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        """
        p = np.sum(testData, axis=0) / (N * n)
        Pbar = np.sum(p ** 2)
        PbarE = Pbar * (1 - Pbar)
        kappa = (Pbar - PbarE) / (1 - PbarE)
        return kappa
```

The kappa method calculates the cohens kappa value of a k-dimensional matrix using the formula:

K = (P - Pbar) / (1 - PbarE)

where P is the observed agreement between raters, Pbar is the expected agreement between raters, and PbarE is the expected agreement between raters and chance.

The fleiss_kappa method calculates the fleiss kappa value of an N * k matrix using the formula:

K = (Pbar - PbarE) / (1 - PbarE)

where Pbar is the mean proportion of each category across all samples, and PbarE is the expected agreement between raters and chance.