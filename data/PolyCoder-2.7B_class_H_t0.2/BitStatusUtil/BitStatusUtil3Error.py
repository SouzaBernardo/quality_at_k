class BitStatusUtil:
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6

        """

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6,2)
        True

        """

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6,2)
        4

        """

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,if not,raise ValueError.
        :param args: Parameters to be checked,list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
       ...
        ValueError: 3 not even
        """

    @staticmethod
    def get_status(states, stat):
        """
        Get the status of the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after getting the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_status(6,2)
        6

        """

    @staticmethod
    def get_status_list(states, stat):
        """
        Get the status of the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after getting the status,list.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_status_list(6,2)
        [6]

        """

    @staticmethod
    def get_status_list_with_index(states, stat, index):
        """
        Get the status of the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :param index: Index of the status,int.
        :return: The status after getting the status,list.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_status_list_with_index(6,2,2)
        [6,2]

        """

    @staticmethod
    def get_status_list_with_index_and_check(states, stat, index, check):
        """
        Get the status of the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :param index: Index of the status,int.
        :param check: Check the status,bool.
        :return: The status after getting the status,list.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_status_list_with_index_and_check(6,2,2,True)
        [6,2]

        """

    @staticmethod
    def get_status_list_with_index_and_check_with_index(states, stat, index, check, index_list):
        """
        Get the status of the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :param index: Index of the status,int.
        :param check: Check the status,bool.
        :param index_list: List of the status,int.
        :return: The status after getting the status,list.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_status_list_with_index_and_check_with_index(6,2,2,True,2)
        [6,2]

        """

    @staticmethod
    def get_status_list_with_index_and_check_with_index_and_check(states, stat, index, check, index_list, check_list):
        """
        Get the status of the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :param index: Index of the status,int.
        :param check: Check the status,bool.
        :param index_list: List of the status,int.
        :param check_list: List of the status,bool.
        :return: The status after getting the status,list.
        >>> bit_status_util = BitStatus