import math
class Statistics3: 


    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5
    
        """
        if len(data) % 2 == 0:
            return (data[0] + data[len(data) - 1]) / 2
        else:
            return data[len(data) / 2]

    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]
    
        >>> statistics3.mode([1, 2, 3, 4, 3])
        [3]
    
        >>> statistics3.mode([1, 2, 3, 3, 4])
        [3]
    
        """
    
    def mode(data):
        if len(data) == 0:
            return []
        else:
            freq = {}
            for num in data:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
            max_freq = max(freq.values())
            return [k for k, v in freq.items() if v == max_freq]

    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0
    
        """
        if len(x) != len(y):
            raise ValueError("The lists must have the same length.")
    
        sum_xy = sum([x[i] * y[i] for i in range(len(x))])
        sum_x = sum([x[i] for i in range(len(x))])
        sum_y = sum([y[i] for i in range(len(y))])
    
        return sum_xy / (sum_x * sum_y)



    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
    
        """
        # code to implement the method

    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0
    
        """
        if not isinstance(data, list):
            raise TypeError("data should be a list")
        if len(data) == 0:
            return 0.0
        return math.sqrt(sum([(x - math.mean(data)) ** 2 for x in data]) / len(data))

    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]
    
        """
        mean = statistics3.mean(data)
        standard_deviation = statistics3.standard_deviation(data)
        z_score = (data - mean) / standard_deviation
        return z_score