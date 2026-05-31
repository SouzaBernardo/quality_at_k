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
        size_of_block = (self.lst[0] + self.limit - 1) // self.limit
        remainder = self.lst[0] % self.limit
        return (size_of_block, remainder)

    def get(self, index):
        size_of_block, remainder = self.setNum()
        start = index * size_of_block
        end = start + size_of_block
        return self.lst[start:end]