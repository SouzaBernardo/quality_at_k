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
        # Calculate the mean and standard deviation of the testData
        mean = np.mean(testData, axis=0)
        std = np.std(testData, axis=0)

        # Calculate the Cohen's kappa value
        k = len(testData)
         kappa = 0.0
        for i in range(k):
            for j in range(i+1, k):
                if np.linalg.norm(testData[i][j] - testData[i][j+1]) < std:
                     kappa += 0.01
         kappa = kappa / k

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
        # Calculate the mean and standard deviation of the testData
        mean = np.mean(testData, axis=0)
        std = np.std(testData, axis=0)
    
        # Calculate the Cohen's kappa value
        k = len(testData)
        kappa = 0.0
        for i in range(k):
            for j in range(i+1, k):
                if np.linalg.norm(testData[i][j] - testData[i][j+1]) < std:
                    kappa += 0.01
        kappa = kappa / k
    
        return kappa