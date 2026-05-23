import numpy as np
from gensim import matutils
from numpy import dot, array
class VectorUtil: 

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
        # normalize the vectors
        vector_1 = matutils.unitvec(array(vector_1))
        vector_2 = matutils.unitvec(array(vector_2))
        
        # compute the cosine similarity
        return dot(vector_1, vector_2)

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
        # normalize the first vector
        vector_1 = matutils.unitvec(array(vector_1))
    
        # normalize all the vectors in vectors_all
        vectors_all = [matutils.unitvec(array(vector)) for vector in vectors_all]
    
        # compute the cosine similarity between vector_1 and each vector in vectors_all
        return [dot(vector_1, vector) for vector in vectors_all]
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
        # normalize all the vectors in vector_list_1 and vector_list_2
        vector_list_1 = [matutils.unitvec(array(vector)) for vector in vector_list_1]
        vector_list_2 = [matutils.unitvec(array(vector)) for vector in vector_list_2]
        
        # compute the mean of vector_list_1 and vector_list_2
        mean_vector_1 = np.mean(vector_list_1, axis=0)
        mean_vector_2 = np.mean(vector_list_2, axis=0)
        
        # compute the cosine similarity between mean_vector_1 and mean_vector_2
        return dot(mean_vector_1, mean_vector_2)
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
        # compute the idf weight for each key in the dictionary
        idf_weight_dict = {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}
        
        return idf_weight_dict