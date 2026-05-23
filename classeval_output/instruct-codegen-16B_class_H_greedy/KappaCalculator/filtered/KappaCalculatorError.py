class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """
    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        """
        # calculate the total number of all elements
        total = np.sum(testData)
        # calculate the number of agreement elements
        agreement = 0
        for i in range(k):
            for j in range(k):
                if i == j:
                    agreement += testData[i][j]
        # calculate the proportion of agreement
        proportion = agreement/total
        # calculate the coefficient
        coefficient = (total*proportion - agreement)/(1 - proportion)
        return coefficient
        @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        """
        # calculate the total number of all elements
        total = np.sum(testData)
        # calculate the number of agreement elements
        agreement = 0
        for i in range(k):
            for j in range(k):
                if i == j:
                    agreement += testData[i][j]
        # calculate the proportion of agreement
        proportion = agreement/total
        # calculate the expected agreement matrix
        exp_agreement_matrix = [[0 for i in range(k)] for j in range(k)]
        for i in range(k):
            for j in range(k):
                exp_agreement_matrix[i][j] = (total*proportion*(1/n))/(total*proportion + (n-1)*(1-proportion))
        # calculate the coefficient
        coefficient = (total*proportion - agreement)/(total*proportion - exp_agreement_matrix[i][j] + (n-1)*(1-proportion))
        return coefficient