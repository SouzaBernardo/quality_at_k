import math
class Statistics3: 


    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        """
        data.sort()
        n = len(data)
        if n % 2 == 0:
            return (data[n//2] + data[n//2-1])/2
        else:
            return data[n//2]

    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
            >>> statistics3.mode([1, 2, 3, 3])
            [3]
    
        """
        count = {}
        for item in data:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        max_count = 0
        for item in count:
            if count[item] > max_count:
                max_count = count[item]
                mode_list = [item]
            elif count[item] == max_count:
                mode_list.append(item)
        return mode_list

    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        """
        n = len(x)
        # Calculate the sums
        sum_x = sum(x)
        sum_y = sum(y)
        # Calculate the sum of the squares
        squared_sum_x = sum([pow(x[i], 2) for i in range(n)])
        squared_sum_y = sum([pow(y[i], 2) for i in range(n)])
        # Calculate the sum of the products
        product_sum = sum([x[i]*y[i] for i in range(n)])
        # Calculate the correlation
        num = product_sum - (sum_x * sum_y/n)
        den = ((squared_sum_x - (pow(sum_x,2) / n)) * (squared_sum_y - (pow(sum_y,2) / n))) ** 0.5
        r = num/den
        return r

    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
            >>> statistics3.mean([1, 2, 3])
            2.0
    
        """
        return sum(data) / len(data)

    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        >>> statistics3 = Statistics3()
            >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
        """

        """

    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]
        """