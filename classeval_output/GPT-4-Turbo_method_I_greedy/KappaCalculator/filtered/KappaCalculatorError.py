import numpy as np
class KappaCalculator: 

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
        n = np.sum(testData)
        p_o = np.sum(np.diag(testData)) / n
        p_e = np.sum(np.sum(testData, axis=0) * np.sum(testData, axis=1)) / (n * n)
        return (p_o - p_e) / (1 - p_e)

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
        P = (np.sum(testData * testData, axis=1) - n) / (n * (n - 1))
        P_bar = np.sum(P) / N
        P_e_bar = np.sum(p * p)
        return (P_bar - P_e_bar) / (1 - P_e_bar)