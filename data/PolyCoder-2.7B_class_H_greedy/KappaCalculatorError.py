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

        if N < 1:
            raise ValueError("N must be greater than 0")

        if n < 1:
            raise ValueError("n must be greater than 0")

        if k > N:
            raise ValueError("k must be less than N")

        if n > N:
            raise ValueError("n must be less than N")

        if k > n:
            raise ValueError("k must be less than n")

        if k == 1:
            return 0.0

        if k == 2:
            return np.sqrt(2)

        if k == 3:
            return np.sqrt(3)

        if k == 4:
            return np.sqrt(4)

        if k == 5:
            return np.sqrt(5)

        if k == 6:
            return np.sqrt(6)

        if k == 7:
            return np.sqrt(7)

        if k == 8:
            return np.sqrt(8)

        if k == 9:
            return np.sqrt(9)

        if k == 10:
            return np.sqrt(10)

        raise ValueError("k must be greater than 10")

    @staticmethod
    def kappa_cohen_kappa(testData, N, k, n):
        """
        Calculate the cohen kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, cohen kappa value
        >>> KappaCalculator.kappa_cohen_kappa([[0, 0, 0, 0, 14],
        >>>                                   [0, 2, 6, 4, 2],
        >>>                                   [0, 0, 3, 5, 6],
        >>>                                   [0, 3, 9, 2, 0],
        >>>                                   [2, 2, 8, 1, 1],
        >>>                                   [7, 7, 0, 0, 0],
        >>>                                   [3, 2, 6, 3, 0],
        >>>                                   [2, 5, 3, 2, 2],
        >>>                                   [6, 5, 2,