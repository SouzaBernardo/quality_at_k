import numpy as np
class KappaCalculator: 


    def kappa(self, testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa(np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]]), 3)
        0.25
        """
        # code to calculate Cohen's kappa

    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss kappa value of an N x k matrix
        :param testData: Input data matrix, N x k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, Fleiss kappa value
        """
        # Get the row indices of each rater
        rater_indices = np.arange(n)
        # Get the row indices of each observation
        observation_indices = testData.row
        # Get the number of common categories for all raters
        common_categories = np.intersect1d(rater_indices, np.arange(k))
        # Calculate the expected counts for each rater
        expected_counts = testData.sum(axis=0)
        # Calculate the observed counts for each rater
        observed_counts = testData.sum(axis=1)
        # Calculate the expected and observed counts for each common category
        expected_observed_counts = expected_counts[common_categories]
        observed_observed_counts = observed_counts[common_categories]
        # Calculate the Fleiss kappa coefficient
        kappa = (observed_observed_counts - expected_observed_counts) / expected_observed_counts
        return kappa