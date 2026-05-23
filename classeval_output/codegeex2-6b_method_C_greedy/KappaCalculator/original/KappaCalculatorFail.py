import numpy as np
class KappaCalculator: 


    @staticmethod
    def kappa(testData, k):
        

        pass


@staticmethod
    def fleiss_kappa(testData, N, k, n):
        

        p_j = np.sum(testData, axis=0) / (N * n)
        p_i = np.sum(testData, axis=1) / (N * n)
        p_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i = np.sum(testData, axis=1) / (N * n)
        p_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j = np.sum(testData, axis=1) / (N * n)
        p_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=1) / (N * n)

        p_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i = np.sum(testData, axis=0) / (N * n)
        p_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j_i_j = np.sum(testData, axis=1) / (N * n)

        p_i_j
