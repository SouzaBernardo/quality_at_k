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
        if n == 0:
            return 0
        if m == 0:
            return 0
        if n == 1:
            return m
        if m == 1:
            return n
        if n == 2:
            return m * (n - 1)
        if m == 2:
            return n * (m - 1)
        if n == 3:
            return m * (n - 1) * (n - 2)
        if m == 3:
            return n * (m - 1) * (m - 2)
        if n == 4:
            return m * (n - 1) * (m - 2) * (n - 3)
        if m == 4:
            return n * (m - 1) * (m - 2) * (m - 3)
        if n == 5:
            return m * (n - 1) * (m - 2) * (m - 3) * (n - 4)
        if m == 5:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4)
        if n == 6:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (n - 5)
        if m == 6:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5)
        if n == 7:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (n - 6)
        if m == 7:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6)
        if n == 8:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (n - 7)
        if m == 8:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7)
        if n == 9:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8)
        if m == 9:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8)
        if n == 10:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9)
        if m == 10:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9)
        if n == 11:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9) * (n - 10)
        if m == 11:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9) * (n - 10)
        if n == 12:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9) * (n - 10) * (n - 11)
        if m == 12:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9) * (n - 10) * (n - 11)
        if n == 13:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9) * (n - 10) * (n - 11) * (n - 12)
        if m == 13:
            return n * (m - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n - 9) * (n - 10) * (n - 11) * (n - 12)
        if n == 14:
            return m * (n - 1) * (m - 2) * (m - 3) * (m - 4) * (m - 5) * (m - 6) * (m - 7) * (n - 8) * (n