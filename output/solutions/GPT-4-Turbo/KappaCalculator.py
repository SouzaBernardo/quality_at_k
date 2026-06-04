import numpy as np
from sklearn.metrics import cohen_kappa_score

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
        # Flatten the matrix and calculate the kappa score
        flattened_data = np.array(testData).flatten()
        return cohen_kappa_score(flattened_data[:k], flattened_data[k:2*k])

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
        # Calculate the total number of ratings
        total_ratings = N * n
        # Calculate the proportion of each category
        p = np.sum(testData, axis=0) / total_ratings
        # Calculate the proportion of ratings for each subject
        P = (np.sum(np.array(testData)**2, axis=1) - n) / (n * (n - 1))
        # Calculate the mean of P
        P_mean = np.mean(P)
        # Calculate the mean of p
        p_mean = np.sum(p**2)
        # Calculate Fleiss' kappa
        kappa = (P_mean - p_mean) / (1 - p_mean)
        return kappa