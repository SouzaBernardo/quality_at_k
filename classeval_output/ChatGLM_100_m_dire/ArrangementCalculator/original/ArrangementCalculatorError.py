import itertools
class ArrangementCalculator: 
    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod






    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        If m is not provided, selects all items.
        :param m: int, the number of items to be chosen (default=None).
        :return: List, a list of arrangements.
        """
        if m is None:
            self.datas.append(list(self.datas))
        else:
             arrangements = []
            for i in range(len(self.datas)):
                if i < m:
                     arrangements.append(self.datas[i])
                else:
                     arrangements.append(self.datas[i - m])
            return arrangements



    def factorial(self, n):
        """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        """
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)