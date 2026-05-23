import numpy as np
from gensim import matutils
from numpy import dot, array
class VectorUtil:  
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """



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
        return dot(vector_1, vector_2) / len(vector_1)





    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        """
        # Calculate the number of unique elements in the number_dict
        unique_count = sum(number_dict.values())
        
        # Calculate the number of elements in the total_num vector
        total_num_elements = total_num * len(number_dict.keys())
        
        # Calculate the number of elements in the count vector
        count_elements = number_dict.values().sum()
        
        # Calculate the number of elements in the count vector
        count_sum = count_elements * len(number_dict.keys())
        
        # Calculate the number of elements in the count vector
        count_div = count_sum / total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_sum = count_div * len(number_dict.keys())
        
        # Calculate the number of elements in the count vector
        count_div_count = count_div_sum * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_sum = count_div_count * total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div = count_div_count_sum / count_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_sum = count_div_count_div * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count = count_div_count_div_sum * total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_sum = count_div_count_div_count * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div = count_div_count_div_count_sum / count_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_sum = count_div_count_div_count_div * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count = count_div_count_div_count_div_sum * total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div = count_div_count_div_count_div_count_sum / count_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_sum = count_div_count_div_count_div_count_div * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count = count_div_count_div_count_div_count_div_sum / count_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count * unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / count_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / total_num_elements
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_div_count_div_count_sum / unique_count
        
        # Calculate the number of elements in the count vector
        count_div_count_div_count_div_count_div_count_sum = count_div_count_div_count_