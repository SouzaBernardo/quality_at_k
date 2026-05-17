import numpy as np
class KappaCalculator: 


    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        pass




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
        N = int(N)
        k = int(k)
        n = int(n)
        if k == 0:
            return 0
        if N == 0:
            return 0
        if N < k:
            return 0
        if k < 0:
            return 0
        if N % k!= 0:
            return 0
        if k % N!= 0:
            return 0
        if N == 1:
            return 1
        if k == 1:
            return 1
        if N == 2:
            return 1
        if k == 2:
            return 1
        if N == 3:
            return 1
        if k == 3:
            return 1
        if N == 4:
            return 1
        if k == 4:
            return 1
        if N == 5:
            return 1
        if k == 5:
            return 1
        if N == 6:
            return 1
        if k == 6:
            return 1
        if N == 7:
            return 1
        if k == 7:
            return 1
        if N == 8:
            return 1
        if k == 8:
            return 1
        if N == 9:
            return 1
        if k == 9:
            return 1
        if N == 10:
            return 1
        if k == 10:
            return 1
        if N == 11:
            return 1
        if k == 11:
            return 1
        if N == 12:
            return 1
        if k == 12:
            return 1
        if N == 13:
            return 1
        if k == 13:
            return 1
        if N == 14:
            return 1
        if k == 14:
            return 1
        if N == 15:
            return 1
        if k == 15:
            return 1
        if N == 16:
            return 1
        if k == 16:
            return 1
        if N == 17:
            return 1
        if k == 17:
            return 1
        if N == 18:
            return 1
        if k == 18:
            return 1
        if N == 19:
            return 1
        if k == 19:
            return 1
        if N == 20:
            return 1
        if k == 20:
            return 1
        if N == 21:
            return 1
        if k