import numpy as np
class KappaCalculator:  
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """



    def kappa(testData, k):
        """Calculate the cohens kappa value of a k-dimensional matrix.
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        # calculate the total number of subjects
        n = len(testData)
        # calculate the number of agreement subjects
        agreement = 0
        for i in range(k):
            for j in range(k):
                agreement += testData[i][j]
        # calculate the proportion of agreement
        proportion = agreement / (n*n)
        # calculate the expected proportion
        e_proportion = 0
        for i in range(k):
            e_proportion += testData[i][i]
        e_proportion = e_proportion / n
        # calculate the kappa value
        kappa = (proportion - e_proportion) / (1 - e_proportion)
        return kappa
        """

    def fleiss_kappa(testData, N, k, n):
        """Calculate the fliss kappa value of an N * k matrix.
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        """
        # calculate the P0, the probability of agreement
        P0 = 0
        for i in range(k):
            P0 += testData[i][i]
        # calculate the P0, the probability of agreement
        P0 = P0 / n
        # calculate the P1, the average probability of all raters
        P1 = 0
        for i in range(N):
            for j in range(k):
                P1 += testData[i][j]
        P1 = P1 / (n * N)
        # calculate the P2, the probability of chance agreement
        P2 = P0 * P1
        # calculate fleiss' kappa value
        fleiss_kappa = (P2 - P0) / (1 - P0)
        return fleiss_kappa