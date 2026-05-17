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

        if k < 1:
            raise ValueError("k must be greater than 0")

        if N < k:
            raise ValueError("N must be greater than k")

        if n < k:
            raise ValueError("n must be greater than k")

        if N == k:
            return 0.0

        if N == k + 1:
            return 1.0

        if N == k + 2:
            return 1.0

        if N == k + 3:
            return 1.0

        if N == k + 4:
            return 1.0

        if N == k + 5:
            return 1.0

        if N == k + 6:
            return 1.0

        if N == k + 7:
            return 1.0

        if N == k + 8:
            return 1.0

        if N == k + 9:
            return 1.0

        if N == k + 10:
            return 1.0

        if N == k + 11:
            return 1.0

        if N == k + 12:
            return 1.0

        if N == k + 13:
            return 1.0

        if N == k + 14:
            return 1.0

        if N == k + 15:
            return 1.0

        if N == k + 16:
            return 1.0

        if N == k + 17:
            return 1.0

        if N == k + 18:
            return 1.0

        if N == k + 19:
            return 1.0

        if N == k + 20:
            return 1.0

        if N == k + 21:
            return 1.0

        if N == k + 22:
            return 1.0

        if N == k + 23:
            return 1.0

        if N == k + 24:
            return 1.0

        if N == k + 25:
            return 1.0

        if N == k + 26:
            return 1.0

        if N == k + 27:
            return 1.0

        if N == k + 28:
            return 1.0

        if N == k + 29:
            return 1.0

        if N == k + 30:
            return 1.0

        if N == k + 31:
            return 1.0

        if N == k + 32:
            return 1.0

        if