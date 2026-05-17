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


    def get_start_end(self, index):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end(0)
        [1, 2]

        """


    def get_start_end_index(self, index):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end_index(0)
        [1, 2]

        """


    def get_start_end_index_by_index(self, index):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end_index_by_index(0)
        [1, 2]

        """


    def get_start_end_index_by_index_and_length(self, index, length):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :param length: the length of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end_index_by_index_and_length(0, 2)
        [1, 2]

        """


    def get_start_end_index_by_index_and_length_by_index(self, index, length):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :param length: the length of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end_index_by_index_and_length_by_index(0, 2)
        [1, 2]

        """


    def get_start_end_index_by_index_and_length_by_index_and_length(self, index, length, length):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :param length: the length of the partition,int.
        :param length: the length of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end_index_by_index_and_length_by_index_and_length(0, 2, 2)
        [1, 2]

        """


    def get_start_end_index_by_index_and_length_by_index_and_length_and_length(self, index, length, length, length):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :param length: the length of the partition,int.
        :param length: the length of the partition,int.
        :param length: the length of the partition,int.
        :return: the corresponding start and end positions, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get_start_end_index_by_index_and_length_by_index_and_length_and_length(0, 2, 2, 2)
        [1, 2]

        """


    def get_start_end_index_by_index_and_length_by_index_and_length_and_length_and_length(self, index, length, length, length, length):
        """
        calculate the start and end positions of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the