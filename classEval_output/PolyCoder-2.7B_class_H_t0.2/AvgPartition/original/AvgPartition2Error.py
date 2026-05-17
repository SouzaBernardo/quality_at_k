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


    def get_size(self):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_size()
        (2, 0)

        """


    def get_start_pos(self):
        """
        calculate the start position of each block and the remainder of the division, and calculate the corresponding end position based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_pos()
        [1, 2]

        """


    def get_end_pos(self):
        """
        calculate the end position of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_end_pos()
        [3, 4]

        """


    def get_size_of_each_block(self):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_size_of_each_block()
        [2, 0]

        """


    def get_start_pos_of_each_block(self):
        """
        calculate the start position of each block and the remainder of the division, and calculate the corresponding end position based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_pos_of_each_block()
        [1, 2]

        """


    def get_end_pos_of_each_block(self):
        """
        calculate the end position of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_end_pos_of_each_block()
        [3, 4]

        """


    def get_size_of_each_block_of_each_block(self):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_size_of_each_block_of_each_block()
        [2, 0]

        """


    def get_start_pos_of_each_block_of_each_block(self):
        """
        calculate the start position of each block and the remainder of the division, and calculate the corresponding end position based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_pos_of_each_block_of_each_block()
        [1, 2]

        """


    def get_end_pos_of_each_block_of_each_block(self):
        """
        calculate the end position of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_end_pos_of_each_block_of_each_block()
        [3, 4]

        """


    def get_size_of_each_block_of_each_block(self):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_size_of_each_block_of_each_block()
        [2, 0]

        """


    def get_start_pos_of_each_block_of_each_block(self):
        """
        calculate the start position of each block and the remainder of the division, and calculate the corresponding end position based on the index of the partition.
  