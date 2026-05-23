import numpy as np
class KappaCalculator: 


    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        """
        # Calculate the observed agreement
        observed_agreement = 0
        for i in range(k):
            for j in range(i+1, k):
                observed_agreement += np.sum(np.diagonal(testData, i, j))
        observed_agreement = observed_agreement / (k * (k - 1) / 2)
        # Calculate the expected agreement
        expected_agreement = 0
        for i in range(k):
            for j in range(i+1, k):
                expected_agreement += (k * (k - 1) / 2) * (testData[i][j] + testData[j][i])
        # Calculate the cohens kappa value
        kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa

    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        """
        # Calculate the observed agreement rate
        p_o = np.sum(np.sum(testData, axis=0)) / (N * k)
        # Calculate the expected agreement rate
        k_i = np.sum(testData, axis=1)
        p_e = (N ** 2) / (n ** 2) * np.sum(k_i * (k_i - 1)) / 2
        # Calculate the fleiss kappa value
        kappa = (p_o - p_e) ** 2 / (1 - p_e)
        return kappa