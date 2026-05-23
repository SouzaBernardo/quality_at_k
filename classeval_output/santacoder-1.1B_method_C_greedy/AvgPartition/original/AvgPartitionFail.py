
class AvgPartition: 
    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions, and check if the number of partitions is greater than 0.
        """
        self.lst = lst
        self.limit = limit



    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)

        """
        if self.limit > 0:
            self.size = len(self.lst) / self.limit
            self.remainder = len(self.lst) % self.limit
        else:
            self.size = 0
            self.remainder = 0
        return self.size, self.remainder


    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
        block = []
        remainder = self.limit - index * self.limit
        for i in range(index * self.limit, (index + 1) * self.limit):
            block.append(self.lst[i])
        return block, remainder
