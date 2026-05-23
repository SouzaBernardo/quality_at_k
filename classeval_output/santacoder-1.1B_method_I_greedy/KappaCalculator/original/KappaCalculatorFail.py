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
        # Calculate the sum of the squared difference between the k-dimensional matrix and the k-dimensional matrix of the same dimension
        sum_squared_difference = 0
        for i in range(k):
            for j in range(k):
                sum_squared_difference += (testData[i][j] - testData[j][i]) ** 2
        # Calculate the square root of the sum of the squared difference
        kappa = np.sqrt(sum_squared_difference / (k * (k - 1)))
        return kappa


    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        # Calculate the sum of the squared difference between the k-dimensional matrix and the k-dimensional matrix of the same dimension
        sum_squared_difference = 0
        for i in range(k):
            for j in range(k):
                sum_squared_difference += (testData[i][j] - testData[j][i]) ** 2
        # Calculate the square root of the sum of the squared difference
        kappa = np.sqrt(sum_squared_difference / (k * (k - 1)))
        # Calculate the number of raters
        n_raters = n * k
        # Calculate the number of raters that have the same value in the k-dimensional matrix
        n_raters_same_value = 0
        for i in range(k):
            for j in range(k):
                if testData[i][j] == testData[j][i]:
                    n_raters_same_value += 1
        # Calculate the number of raters that have different values in the k-dimensional matrix
        n_raters_different_value = 0
        for i in range(k):
            for j in range(k):
                if testData[i][j]!= testData[j][i]:
                    n_raters_different_value += 1
        # Calculate the number of raters that have the same value in the k-dimensional matrix divided by the number of raters
        n_raters_same_value_ratio = n_raters_same_value / n_raters
        # Calculate the number of raters that have different values in the k-dimensional matrix divided by the number of raters
        n_raters_different_value_ratio = n_raters_different_value / n_raters
        # Calculate the fleiss kappa value
        fleiss_kappa = kappa * (n_raters_same_value_ratio / (n_raters_same_value_ratio + n_raters_different_value_ratio))
        return fleiss_kappa
