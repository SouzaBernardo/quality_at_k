import math
from typing import List
import unittest
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
    
        :param n: The total number of elements, int.
        :param m: The number of elements in each combination, int.
        :return: The number of combinations, int.
        >>> CombinationCalculator.count(4, 2)
            6
        """
        combinations = 1
        for i in range(1, n // m + 1):
            combinations *= m
        return combinations

    def count_all(n: int) -> float:
        """
        Calculate the number of all possible combinations.
    
        :param n: The total number of elements, int.
        :return: The number of all possible combinations, float, if the number of combinations is greater than 2^63-1, return float("inf").
        >>> CombinationCalculator.count_all(4)
        15.0
        """
        if n > 2 ** 63 - 1:
            return float("inf")
        combinations = 1
        for i in range(1, n):
            combinations *= i
        return combinations

    def select(m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
    
        :param m: The number of elements in each combination, int.
        :return: A list of combinations, List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
        combinations = 1
        for i in range(1, m):
            combinations *= i
            yield [self.datas[i * m // 2]]

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of  selecting elements from the given data list,and it uses the select method.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
        return [list(combination) for combination in self.select(len(self.datas))]

