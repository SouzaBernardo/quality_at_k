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
            raise ValueError("index must be >= 0")

        if index >= len(self.lst):
            raise ValueError("index must be less than the number of partitions")

        if index == 0:
            return [self.lst[0]]

        if index == len(self.lst) - 1:
            return [self.lst[-1]]

        start = self.lst[index - 1]
        end = self.lst[index]

        return [start, end]

    def getStart(self):
        """
        calculate the start position of each block, and return the corresponding end position.
        :return: the corresponding end position.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.getStart()
        2
        >>> a.getStart()
        3
        >>> a.getStart()
        4
        >>> a.getStart()
        5
        >>> a.getStart()
        6
        >>> a.getStart()
        7
        >>> a.getStart()
        8
        >>> a.getStart()
        9
        >>> a.getStart()
        10
        >>> a.getStart()
        11
        >>> a.getStart()
        12
        >>> a.getStart()
        13
        >>> a.getStart()
        14
        >>> a.getStart()
        15
        >>> a.getStart()
        16
        >>> a.getStart()
        17
        >>> a.getStart()
        18
        >>> a.getStart()
        19
        >>> a.getStart()
        20
        >>> a.getStart()
        21
        >>> a.getStart()
        22
        >>> a.getStart()
        23
        >>> a.getStart()
        24
        >>> a.getStart()
        25
        >>> a.getStart()
        26
        >>> a.getStart()
        27
        >>> a.getStart()
        28
        >>> a.getStart()
        29
        >>> a.getStart()
        30
        >>> a.getStart()
        31
        >>> a.getStart()
        32
        >>> a.getStart()
        33
        >>> a.getStart()
        34
        >>> a.getStart()
        35
        >>> a.getStart()
        36
        >>> a.getStart()
        37
        >>> a.getStart()
        38
        >>> a.getStart()
        39
        >>> a.getStart()
        40
        >>> a.getStart()
        41
        >>> a.getStart()
        42
        >>> a.getStart()
        43
        >>> a.getStart()
        44
        >>> a.getStart()
        45
        >>> a.getStart()
        46
        >>> a.getStart()
        47
        >>> a.getStart()
        48
        >>> a.getStart()
        49
        >>> a.getStart()
        50
        >>> a.getStart()
        51
        >>> a.getStart()
        52
        >>> a.getStart()
        53
        >>> a.getStart()
        54
        >>> a.getStart()
        55
        >>> a.getStart()
        56
        >>> a.getStart()
        57
        >>> a.getStart()
        58
        >>> a.getStart()
        59
        >>> a.getStart()
        60
        >>> a.getStart()
        61
        >>> a.getStart()
