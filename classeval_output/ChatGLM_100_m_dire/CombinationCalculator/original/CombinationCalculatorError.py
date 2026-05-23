import math
from typing import List
import unittest
class CombinationCalculator: 
    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        """
        self.datas = datas

    @staticmethod


    def count(self, n: int, m: int) -> int:
        """
        Calculate the number of combinations for a specific count.
        :param n: The total number of elements,int.
        :param m: The number of elements in each combination,int.
        :return: The number of combinations,int.
        >>> CombinationCalculator.count(4, 2)
        6
        """
        count = self.count_all(n, m)
        if count > 2^63-1:
            return float("inf")
        return count

    def count_all(self, n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: The total number of elements,int.
        :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
        """
        if n > 2**63-1:
            return float("inf")
        
        count = 0
        result = []
        for i in range(n):
            for j in range(i):
                result.append(self._select(i, resultList=[self.datas[j]], j, self.datas[j]))
            count += len(result)
        return count

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
        pass


    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of  selecting elements from the given data list,and it uses the select method.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
    
        """
        return self.datas.select(self.datas.size)

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex: The index of the data to be selected,int.
        :param resultList: The list of elements in the combination,List[str].
        :param resultIndex: The index of the element in the combination,int.
        :param result: The list of combinations,List[List[str]].
        :return: None.
        """
        if dataIndex < 0 or dataIndex >= len(self.datas):
            raise ValueError("dataIndex must be a non-negative integer and not greater than the length of the datas")
        if resultList == [None]:
            result = self.select(dataIndex, self.datas[dataIndex], resultIndex, self.datas[dataIndex])
        else:
            result = self.select(dataIndex, resultList, resultIndex, self.datas[dataIndex])
        if result == [None]:
            return None
        return result