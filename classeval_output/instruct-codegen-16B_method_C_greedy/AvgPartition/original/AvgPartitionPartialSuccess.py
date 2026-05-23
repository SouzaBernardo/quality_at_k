
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
        length = len(self.lst)
        partition_size, remainder = divmod(length, self.limit)
        return (partition_size, remainder)

    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        """
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        start = size * index
        end = start + size
        if index == self.limit - 1:
            end += remainder
        return self.lst[start:end]