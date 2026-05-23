
class AvgPartition: 
    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions, and check if the number of partitions is greater than 0.
        """
        self.lst = lst
        self.limit = limit



    def setNum(self):
        size_of_block = (self.limit - len(self.lst)) // len(self.lst)
        remainder = (self.limit - len(self.lst)) % len(self.lst)
        return (size_of_block, remainder)

    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
        if self.limit > 0:
            block_size = int(len(self.lst) / self.limit)
            start = index * block_size
            end = start + block_size
            return self.lst[start:end]
        else:
            return []