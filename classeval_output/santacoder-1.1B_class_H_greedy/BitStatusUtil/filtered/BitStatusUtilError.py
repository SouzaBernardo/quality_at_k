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
    def get_bit_status(states, bit):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit: Specified bit,int.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status(6,2)
        4

        """

    @staticmethod
    def get_bit_status_list(states, bit_list):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_list: Specified bit list,list.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_list(6,[2,3,4])
        [4, 4, 4]

        """

    @staticmethod
    def get_bit_status_set(states, bit_set):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set: Specified bit set,set.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_list_set(states, bit_list_set):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_list_set: Specified bit list set,set.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_list_set(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list(states, bit_set_list):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list: Specified bit set list,list.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set_list(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list_set(states, bit_set_list_set):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list_set: Specified bit set list set,set.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set_list_set(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list_set_list(states, bit_set_list_set_list):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list_set_list: Specified bit set list set list,list.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set_list_set_list(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list_set_list_set(states, bit_set_list_set_list_set):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list_set_list_set: Specified bit set list set list set,set.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set_list_set_list_set(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list_set_list_set_list(states, bit_set_list_set_list_set_list):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list_set_list_set_list: Specified bit set list set list set list,list.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set_list_set_list_set_list(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list_set_list_set_list_set(states, bit_set_list_set_list_set_list_set):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list_set_list_set_list_set: Specified bit set list set list set list set,set.
        :return: The status of the specified bit,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.get_bit_status_set_list_set_list_set_list_set(6,[2,3,4])
        {2, 3, 4}

        """

    @staticmethod
    def get_bit_status_set_list_set_list_set_list_set_list(states, bit_set_list_set_list_set_list_set_list):
        """
        Get the status of the specified bit in the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param bit_set_list_set_list_set_list_set_list: Specified bit set list set list set list set list,list.
        :return: The status of the specified bit,int.
        >>> bit_