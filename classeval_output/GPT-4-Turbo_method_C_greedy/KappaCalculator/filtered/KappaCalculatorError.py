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
        # Flatten the matrix
        flattened_data = np.array(testData).flatten()
        # Calculate the kappa value
        kappa_value = cohen_kappa_score(flattened_data, flattened_data)
        return kappa_value

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
        testData = np.array(testData)
        pj = np.sum(testData, axis=0) / (N * n)
        Pi = (np.sum(testData * testData, axis=1) - n) / (n * (n - 1))
        Pbar = np.sum(Pi) / N
        PbarE = np.sum(pj * pj)
        kappa = (Pbar - PbarE) / (1 - PbarE)
        return kappa