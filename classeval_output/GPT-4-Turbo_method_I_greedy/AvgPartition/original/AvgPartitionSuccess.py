
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
        """
        if self.limit > 0:
            block_size = len(self.lst) // self.limit
            remainder = len(self.lst) % self.limit
            return block_size, remainder
        else:
            return "Error: Number of partitions must be greater than 0"
    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        """
        block_size, remainder = self.setNum()
        if index < remainder:
            start = index * (block_size + 1)
            end = start + block_size + 1
        else:
            start = index * block_size + remainder
            end = start + block_size
        return self.lst[start:end]
