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
        return np.sum(testData * np.log(testData) / np.log(k))




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
        if n == 0:
            return 0.0
        if k == 0:
            return 0.0
        if k == 1:
            return 1.0
        if k == 2:
            return 1.0
        if k == 3:
            return 1.0
        if k == 4:
            return 1.0
        if k == 5:
            return 1.0
        if k == 6:
            return 1.0
        if k == 7:
            return 1.0
        if k == 8:
            return 1.0
        if k == 9:
            return 1.0
        if k == 10:
            return 1.0
        if k == 11:
            return 1.0
        if k == 12:
            return 1.0
        if k == 13:
            return 1.0
        if k == 14:
            return 1.0
        if k == 15:
            return 1.0
        if k == 16:
            return 1.0
        if k == 17:
            return 1.0
        if k == 18:
            return 1.0
        if k == 19:
            return 1.0
        if k == 20:
            return 1.0
        if k == 21:
            return 1.0
        if k == 22:
            return 1.0
        if k == 23:
            return 1.0
        if k == 24:
            return 1.0
        if k == 25:
            return 1.0
        if k == 26:
            return 1.0
        if k == 27:
            return 1.0
        if k == 28:
            return 1.0
        if k == 29:
            return 1.0
        if k == 30:
            return 1.0
        if k == 31:
            return 1.0
        if k == 32:
            return 1.0
        if k == 33:
            return 1.0
        if k == 34:
            return 1.0
        if k == 35:
            return 1.0
        if k == 36:
            return 1.0
        if k == 37:
            return 1.0
        if k == 38:
            return 1.0
        if k == 39:
            return 1.0
        if k == 40:
            return 1.0
        if k == 41:
            return 1.0
        if k == 42:
            return 1.0
      