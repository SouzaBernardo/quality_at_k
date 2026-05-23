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



K = (P - Pbar) / (1 - PbarE)

where P is the observed agreement between raters, Pbar is the expected agreement between raters, and PbarE is the expected agreement between raters and chance.


K = (Pbar - PbarE) / (1 - PbarE)

where Pbar is the mean proportion of each category across all samples, and PbarE is the expected agreement between raters and chance.