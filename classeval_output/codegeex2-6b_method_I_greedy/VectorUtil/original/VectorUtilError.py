import numpy as np
from gensim import matutils
from numpy import dot, array
class VectorUtil:  
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """



    @staticmethod
    def similarity(vector_1, vector_2):
        
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))


    def cosine_similarities(vector_1, vectors):


@staticmethod
    def cosine_similarities(vector_1, vectors_all):


@staticmethod
    def n_similarity(vector_list_1, vector_list_2):


@staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
