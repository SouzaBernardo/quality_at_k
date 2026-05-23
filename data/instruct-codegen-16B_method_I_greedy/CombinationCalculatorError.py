import math
from typing import List
class CombinationCalculator:  
    """
    This is a class that provides methods to calculate the number of combinations for a specific count, calculate all possible combinations, and generate combinations with a specified number of elements.
    """

    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        """
        self.datas = datas

    @staticmethod


    def count(n: int, m: int) -> int:
        """Calculate the number of combinations for a specific count.
        :param n: The total number of elements,int.
        :param m: The number of elements in each combination,int.
        :return: The number of combinations,int.
        """
        return math.comb(n, m)
        """

    def count_all(n):
        if n > 2**63-1:
            return float("inf")
        else:
            return math.comb(n, n)

        """

    def select_all(self):
        result = []
        for i in range(1, len(self.datas)+1):
            result.extend(self.select(i))
        return result


        """