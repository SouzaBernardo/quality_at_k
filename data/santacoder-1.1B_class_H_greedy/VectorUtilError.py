import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vector_2: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """


    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """


    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """


    @staticmethod
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


    @staticmethod
    def compute_idf_weight(total_num, count):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param count: int
        :return: float
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight(2, 1)
        1.0033021088637848
        """


    @staticmethod
    def compute_idf_weight_list(total_num, number_list):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_list: list
        :return: list
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_list(2, [1, 2])
        [1.0033021088637848, 0.6931471805599453]
        """


    @staticmethod
    def compute_idf_weight_array(total_num, number_array):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_array: numpy.ndarray
        :return: numpy.ndarray
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_array(2, np.array([1, 2]))
        array([1.0033021088637848, 0.6931471805599453])
        """


    @staticmethod
    def compute_idf_weight_mat(total_num, number_mat):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_mat: numpy.ndarray
        :return: numpy.ndarray
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_mat(2, matutils.unitvec(np.array([1, 2])))
        array([1.0033021088637848, 0.6931471805599453])
        """


    @staticmethod
    def compute_idf_weight_list_mat(total_num, number_list_mat):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_list_mat: list of numpy.ndarray
        :return: list of numpy.ndarray
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_list_mat(2, [[1, 2], [3, 4]])
        [[1.0033021088637848, 0.6931471805599453], [0.9999999999999999, 0.00000000000000001]]
        """


    @staticmethod
    def compute_idf_weight_array_mat(total_num, number_array_mat):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_array_mat: numpy.ndarray
        :return: numpy.ndarray
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_array_mat(2, np.array([[1, 2], [3, 4]]))
        array([[1.0033021088637848, 0.6931471805599453],
               [0.9999999999999999, 0.00000000000000001]])
        """


    @staticmethod
    def compute_idf_weight_mat_list(total_num, number_mat_list):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_mat_list: list of numpy.ndarray
        :return: list of numpy.ndarray
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_mat_list(2, [[1, 2], [3, 4]])
        [[1.0033021088637848, 0.6931471805599453], [0.9999999999999999, 0.00000000000000001]]
        """


    @staticmethod
    def compute_idf_weight_mat_array(total_num,