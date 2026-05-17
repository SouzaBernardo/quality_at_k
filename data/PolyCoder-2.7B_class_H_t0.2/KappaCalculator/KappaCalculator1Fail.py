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

        if k > N:
            raise ValueError("k must be less than N")

        if n < 1:
            raise ValueError("n must be greater than 0")

        if n > N:
            raise ValueError("n must be less than N")

        if k == 0:
            return 0.0

        if k == 1:
            return 1.0

        if k == 2:
            return np.sqrt(2.0 / (N - 1))

        if k == 3:
            return np.sqrt(2.0 / (N - 2))

        if k == 4:
            return np.sqrt(2.0 / (N - 3))

        if k == 5:
            return np.sqrt(2.0 / (N - 4))

        if k == 6:
            return np.sqrt(2.0 / (N - 5))

        if k == 7:
            return np.sqrt(2.0 / (N - 6))

        if k == 8:
            return np.sqrt(2.0 / (N - 7))

        if k == 9:
            return np.sqrt(2.0 / (N - 8))

        if k == 10:
            return np.sqrt(2.0 / (N - 9))

        if k == 11:
            return np.sqrt(2.0 / (N - 10))

        if k == 12:
            return np.sqrt(2.0 / (N - 11))

        if k == 13:
            return np.sqrt(2.0 / (N - 12))

        if k == 14:
            return np.sqrt(2.0 / (N - 13))

        if k == 15:
            return np.sqrt(2.0 / (N - 14))

        if k == 16:
            return np.sqrt(2.0 / (N - 15))

        if k == 17:
            return np.sqrt(2.0 / (N - 16))

        if k == 18:
            return np.sqrt(2.0 / (N - 17))

        if k == 19:
            return np.sqrt(2.0 / (N - 18))

        if k == 20:
            return np.sqrt(2.0 / (N - 19))

        if k == 21:
            return np.sqrt(2.0 / (N - 20))

        if k == 22:
            return np.sqrt(2.0 / (N - 21))

        if k == 23:
            return np.sqrt(2.0 / (N - 22))

        if k == 24:
            return np.sqrt(2.0 / (N - 23))

        if k == 25:
            return np.sqrt(2.0 / (N - 24))