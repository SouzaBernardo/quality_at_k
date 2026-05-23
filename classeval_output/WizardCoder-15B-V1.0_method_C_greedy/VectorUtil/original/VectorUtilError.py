import numpy as np
from gensim import matutils
from numpy import dot, array
class VectorUtil: 


    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vector_2: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
        """
        return dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2))

    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        """
        vector_1 = matutils.unitvec(vector_1)
        vectors_all = [matutils.unitvec(v) for v in vectors_all]
        return [dot(vector_1, v) for v in vectors_all]

    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        """
        vectors_1 = matutils.corpus2dense(vector_list_1, num_terms=len(vector_list_1[0])).T
        vectors_2 = matutils.corpus2dense(vector_list_2, num_terms=len(vector_list_2[0])).T
        return dot(vectors_1, vectors_2.T) / (array([linalg.norm(vectors_1, axis=1)]).T * array([linalg.norm(vectors_2, axis=1)]).T)

    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        """
        idf_dict = {}
        for word, count in number_dict.items():
            idf_dict[word] = np.log(total_num + 1) - np.log(count + 1)
        return idf_dict