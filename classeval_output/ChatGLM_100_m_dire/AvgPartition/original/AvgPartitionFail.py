
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
        num_blocks = len(self.lst) // self.limit
        rem = num_blocks - (num_blocks % self.limit)
        return (rem, self.lst[rem])

    def get(self, index):
        size = self.lst.count(index)
        remainder = size // self.limit
        start = index + remainder
        end = start + self.limit
        return [self.lst[start:end]]