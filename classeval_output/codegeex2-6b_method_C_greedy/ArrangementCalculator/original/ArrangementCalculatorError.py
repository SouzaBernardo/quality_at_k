import itertools
class ArrangementCalculator: 
    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod


    @staticmethod
    def count(n, m=None):
        

        if m is None:
            return ArrangementCalculator.factorial(n)
        else:
            return ArrangementCalculator.factorial(n) / ArrangementCalculator.factorial(n - m)

    def select(self, m=None):


@staticmethod
    def count_all(n):
        

        return int(factorial(n) / (factorial(n - m) * factorial(m)))


    def select(self, m=None):
        

        if m is None:
            m = len(self.datas)

        return list(itertools.combinations(self.datas, m))


    def select_all(self):


@staticmethod
    def factorial(n):
