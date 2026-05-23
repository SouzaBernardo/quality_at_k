import numpy as np
class KappaCalculator: 


    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        """
        # Calculate the number of categories in each dimension
        n_rows = len(testData)
        n_cols = len(testData[0])
        # Calculate the number of categories in the matrix
        n_total = n_rows * n_cols
        # Calculate the number of categories in each group
        n_groups = k**2
        # Calculate the number of elements in each group
        n_elements = n_total // n_groups
        # Calculate the number of elements in each category
        n_elements_per_group = n_elements // k
        # Calculate the number of elements in the matrix
        n_elements_total = n_rows * n_cols
        # Calculate the sum of squares of the elements in each group
        ss_group = (n_elements_per_group - 1) * (n_elements_per_group - 1) * (n_elements_total - n_elements_per_group)
        # Calculate the sum of squares of the elements in the matrix
        ss_total = (n_elements_total - 1) * (n_elements_total - 1) * (n_total - n_elements_total)
        # Calculate the variance of the elements in each group
        var_group = ss_group / (n_elements_per_group - 1)
        # Calculate the variance of the elements in the matrix
        var_total = ss_total / (n_elements_total - 1)
        # Calculate the kappa value
        kappa = (var_group - var_total) / (1 - var_total)
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
        # Calculate P0 (the chance agreement)
        P0 = np.sum(np.sum(testData == 0)) / (N * n)
        # Calculate P1 (the chance of the rater's agreement)
        P1 = np.sum([np.sum(testData[:, i] == 0)**2 / (np.sum(testData[:, i] == 0) * np.sum(testData[:, i] == 1)) for i in range(k)])
        # Calculate P2 (the chance of the raters agreeing on the category)
        P2 = np.sum([np.sum(testData[:, i] == 0)**2 / (np.sum(testData[:, i] == 0) * np.sum(testData[:, i] == 2)) for i in range(k)])
        # Calculate P3 (the chance of the raters randomly agreeing on the category)
        P3 = np.sum([np.sum(testData[:, i] == 0)**2 / (np.sum(testData[:, i] == 0) * np.sum(testData[:, i] == 3)) for i in range(k)])
        # Calculate Fleiss' Kappa
        return (P0 - P1) / (P0 - P1 - P2 + P3)