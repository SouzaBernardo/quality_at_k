import numpy as np
class KappaCalculator: 


    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator. kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        # Calculate the kappa value of each row
         kappa_row = []
        for i in range(N):
             kappa_row.append(np.fleiss_kappa(testData[:, i], k, n))
        # Calculate the total kappa value
         kappa = sum( kappa_row )
        return kappa