import numpy as np
class KappaCalculator: 


    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        # Calculate the number of rows and columns of the matrix
        n = testData.shape[0]
        m = testData.shape[1]
        # Calculate the number of non-zero elements in the matrix
        nnz = np.count_nonzero(testData)
        # Calculate the number of non-zero elements in the matrix divided by the number of rows and columns
        nnz_ratio = nnz / (n * m)
        # Calculate the number of non-zero elements in the matrix divided by the number of rows
        nnz_ratio_row = nnz_ratio / m
        # Calculate the number of non-zero elements in the matrix divided by the number of columns
        nnz_ratio_col = nnz_ratio / n
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix
        nnz_ratio_all = nnz_ratio / (n * m * nnz)
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of rows
        nnz_ratio_all_row = nnz_ratio_all / m
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of columns
        nnz_ratio_all_col = nnz_ratio_all / n
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of rows and columns
        nnz_ratio_all_all = nnz_ratio_all / (n * m * nnz * m * n)
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of rows
        nnz_ratio_all_all_row = nnz_ratio_all_all / m
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of columns
        nnz_ratio_all_all_col = nnz_ratio_all_all / n
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of rows and columns
        nnz_ratio_all_all_all = nnz_ratio_all_all / (n * m * nnz * m * n * m)
        # Calculate the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero elements in the matrix divided by the number of non-zero

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
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k = len(set(testData[:, -1]))
        # Calculate the number of raters
        n = len(testData)
        # Calculate the number of categories
        k =