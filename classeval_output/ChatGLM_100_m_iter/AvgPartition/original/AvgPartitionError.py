
class AvgPartition:  
    """
    This is a class that partitions the given list into different blocks by specifying the number of partitions, with each block having a uniformly distributed length.
    """

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
        """
        num_partitions = len(self.lst) // self.limit
        num_partitions += self.limit - 1
        block_size = num_partitions * self.lst.index(self.lst.index(self.lst[-1]))
        remainder = num_partitions - self.limit
        return (block_size, remainder)

    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
        block = self.setNum()
        start = index // block_size
        end = index % block_size
        return [start, end]