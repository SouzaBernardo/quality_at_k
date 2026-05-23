import itertools
class ArrangementCalculator:  
    """
    The Arrangement class provides permutation calculations and selection operations for a given set of data elements.
    """

    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod


    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :param n: int, the total number of items.
        :param m: int, the number of items to be chosen (default=None).
        :return: int, the count of arrangements.
        >>> ArrangementCalculator.count(5, 3)
            60
    
        """
        if m is None:
            m = n
        return factorial(n) / factorial(m)

    def count_all(n):
        count = 0
        for i in range(1, n+1):
            count += ArrangementCalculator.count(n, i)
        return count

    def select(m=None):
        if m is None:
            m = len(self.datas)
        return [self.datas[i] for i in range(m)]

    def select_all(m=None):
        if m is None:
            m = len(self.datas)
        return [self.datas[i] for i in range(m)]

    def factorial(n):
        """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        >>> ArrangementCalculator.factorial(4)
            24
        """
        if n == 0:
            return 1
        else:
            return n * ArrangementCalculator.factorial(n-1)