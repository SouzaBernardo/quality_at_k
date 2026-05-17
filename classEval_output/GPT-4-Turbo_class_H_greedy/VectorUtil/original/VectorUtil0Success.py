```python
import numpy as np
from gensim import matutils
from numpy import dot, array
import math

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        vectors_all = np.array(vectors_all)
        return np.dot(matutils.unitvec(vector_1), matutils.unitvec(vectors_all).T)

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        vector_list_1 = np.array(vector_list_1)
        vector_list_2 = np.array(vector_list_2)
        return np.dot(matutils.unitvec(vector_list_1.mean(axis=0)), matutils.unitvec(vector_list_2.mean(axis=0)))

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        return {key: math.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}
```