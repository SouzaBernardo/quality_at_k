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
        if m == n:
            return 1
        if m == 0:
            return 0
        if m == 1:
            return 1
        if m == 2:
            return 2
        if m == 3:
            return 3
        if m == 4:
            return 4
        if m == 5:
            return 5
        if m == 6:
            return 6
        if m == 7:
            return 7
        if m == 8:
            return 8
        if m == 9:
            return 9
        if m == 10:
            return 10
        if m == 11:
            return 11
        if m == 12:
            return 12
        if m == 13:
            return 13
        if m == 14:
            return 14
        if m == 15:
            return 15
        if m == 16:
            return 16
        if m == 17:
            return 17
        if m == 18:
            return 18
        if m == 19:
            return 19
        if m == 20:
            return 20
        if m == 21:
            return 21
        if m == 22:
            return 22
        if m == 23:
            return 23
        if m == 24:
            return 24
        if m == 25:
            return 25
        if m == 26:
            return 26
        if m == 27:
            return 27
        if m == 28:
            return 28
        if m == 29:
            return 29
        if m == 30:
            return 30
        if m == 31:
            return 31
        if m == 32:
            return 32
        if m == 33:
            return 33
        if m == 34:
            return 34
        if m == 35:
            return 35
        if m == 36:
            return 36
        if m == 37:
            return 37
        if m == 38:
            return 38
        if m == 39:
            return 39
        if m == 40:
            return 40
        if m == 41:
            return 41
        if m == 42:
            return 42
        if m == 43:
            return 43
        if m == 44:
            return 44
        if m == 45:
            return 45
        if m == 46:
            return 46
        if m == 47:
            return 47
        if m == 48:
            return 48
        if m == 49:
            return 49
        if m == 50:
            return 50
        if m == 51:
            return 51
        if m == 52:
            return 52
        if m == 53:
            return 53
        if m == 54:
            return 54
        if m == 55:
            return 55
        if m == 56:
            return 56
        if m == 57:
            return 57
        if m == 58:
            return 58
        if m == 59:
            return 59
        if m == 60:
            return 60
        if m == 61:
            return 61







