import itertools
class ArrangementCalculator: 
    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod




    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        >>> ArrangementCalculator.count_all(4)
        64
        """
        return ArrangementCalculator.factorial(n)



    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        """
        return list(itertools.product(self.datas, repeat=len(self.datas)))

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