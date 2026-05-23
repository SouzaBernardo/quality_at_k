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
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
            0.25
        """
        # code to implement the kappa method
        pass

    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss kappa value of an N x k matrix
        :param testData: Input data matrix, N x k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, Fleiss kappa value
        """
        # code to implement the fleiss_kappa method
        pass