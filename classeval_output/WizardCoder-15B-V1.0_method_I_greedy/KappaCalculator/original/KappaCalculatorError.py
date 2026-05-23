import numpy as np
class KappaCalculator:  
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """



    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        """
        n = len(testData)
        p = np.sum(testData, axis=0) / n
        P = np.sum(p * p)
        Pbar = np.sum(p) ** 2 / n
        kappa = (P - Pbar) / (1 - Pbar)
        return float(kappa)

