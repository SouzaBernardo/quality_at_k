import numpy as np
from gensim import matutils
from numpy import dot, array
class VectorUtil: 






    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        array([0.98972875, 0.98972875])
        """
        vectors_1 = [matutils.unitvec(v) for v in vector_list_1]
        vectors_2 = [matutils.unitvec(v) for v in vector_list_2]
        return np.array([dot(v1, v2) for v1, v2 in zip(vectors_1, vectors_2)])

    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
        idf_dict = {}
        for key, count in number_dict.items():
            idf_dict[key] = np.log(total_num + 1 / (count + 1))
        return idf_dict