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
        if n < 2:
            return 1
        if n < 2**m:
            return 1
        return (n // m) * (n // (m-1)) * ... * (n // 2) * (n // 1)

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: The total number of elements,int.
        :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
        if n < 2:
            return 1
        if n < 2**63:
            return 1
        return 2**63

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
        if m == 0:
            return [[] for _ in range(len(self.datas))]
        result = []
        for i in range(len(self.datas)):
            resultList = [self.datas[i]]
            resultIndex = 0
            while resultIndex < m:
                if m - resultIndex >= len(resultList):
                    resultList.append(resultList[-1])
                resultList[resultIndex] = resultList[resultIndex].append(self.datas[i])
                resultIndex += 1
            result.append(resultList)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of  selecting elements from the given data list,and it uses the select method.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]

        """
        result = []
        for i in range(len(self.datas)):
            resultList = [[] for _ in range(len(self.datas))]
            for j in range(len(self.datas)):
                resultList[j] = self.datas[j]
            result.append(resultList)
        return result

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]], m: int):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex