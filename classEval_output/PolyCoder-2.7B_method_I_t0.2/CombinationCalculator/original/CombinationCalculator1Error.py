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
        """
        Calculate the number of combinations for a specific count.
        :param n: The total number of elements,int.
        :param m: The number of elements in each combination,int.
        :return: The number of combinations,int.
        >>> CombinationCalculator.count(4, 2)
        6
        """
        return int(math.ceil(math.log(n, 2) / math.log(m, 2)))


    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: The total number of elements,int.
        :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
        return int(math.ceil(math.log(n, 2)))



    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
        if m > self.count_all(self.count(m)):
            return []
        return [self.datas[i] for i in range(0, m)]



    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of  selecting elements from the given data list,and it uses the select method.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]

        """
        return [self.select(i) for i in range(0, self.count(self.count_all(self.count(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count_all(self.count

