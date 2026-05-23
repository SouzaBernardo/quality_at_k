
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
        
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size, remainder



    def partition(self):


    def get(self, index):
        

        size, remainder = self.setNum()
        start = index * size
        end = start + size
        if index == self.limit - 1:
            end += remainder
        return self.lst[start:end]
