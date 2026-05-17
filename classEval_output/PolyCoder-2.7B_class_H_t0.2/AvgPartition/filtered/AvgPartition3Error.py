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
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)

        """


    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """

        if index < 0:
            return [0, 0]
        elif index >= len(self.lst):
            return [0, 0]
        else:
            return [self.lst[index] - self.lst[index - 1], self.lst[index - 1] + self.lst[index]]


    def getStart(self):
        """
        calculate the start position of the partition, and return the corresponding end position.
        :return: the corresponding end position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getStart()
        3

        """

        return self.get(0)


    def getEnd(self):
        """
        calculate the end position of the partition, and return the corresponding start position.
        :return: the corresponding start position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getEnd()
        4

        """

        return self.get(len(self.lst) - 1)


    def getLength(self):
        """
        calculate the length of the partition, and return the corresponding end position.
        :return: the corresponding end position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getLength()
        4

        """

        return self.getEnd() - self.getStart()


    def getLength(self):
        """
        calculate the length of the partition, and return the corresponding start position.
        :return: the corresponding start position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getLength()
        3

        """

        return self.getLength()


    def getStart(self):
        """
        calculate the start position of the partition, and return the corresponding end position.
        :return: the corresponding end position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getStart()
        3

        """

        return self.getStart() + self.getLength()


    def getEnd(self):
        """
        calculate the end position of the partition, and return the corresponding start position.
        :return: the corresponding start position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getEnd()
        4

        """

        return self.getEnd() - self.getStart()


    def getLength(self):
        """
        calculate the length of the partition, and return the corresponding start position.
        :return: the corresponding start position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getLength()
        4

        """

        return self.getLength()


    def getLength(self):
        """
        calculate the length of the partition, and return the corresponding end position.
        :return: the corresponding end position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getLength()
        3

        """

        return self.getLength()


    def getPartition(self):
        """
        calculate the partition of the given list, and return the corresponding start and end positions.
        :return: the corresponding start and end positions.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getPartition()
        [1, 2]

        """

        return self.getStart(), self.getEnd()


    def getPartition(self):
        """
        calculate the partition of the given list, and return the corresponding start and end positions.
        :return: the corresponding start and end positions.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getPartition()
        [1, 2]

        """

        return self.getStart(), self.getEnd()


    def getPartition(self):
        """
        calculate the partition of the given list, and return the corresponding start and end positions.
        :return: the corresponding start and end positions.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getPartition()
        [1, 2]

        """

        return self.getStart(), self.