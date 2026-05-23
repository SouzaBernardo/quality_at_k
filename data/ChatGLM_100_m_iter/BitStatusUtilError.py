import unittest
class BitStatusUtil:  
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """



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
        if states & (stat - 1):
            raise ValueError("Invalid status")
        elif states & (stat + 1):
            raise ValueError("Invalid status")
        elif states & (stat - 2):
            raise ValueError("Invalid status")
        elif states & (stat + 2):
            raise ValueError("Invalid status")
        return states | (stat - 1)

    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        """
        if states & (stat - 1):
            raise ValueError("Invalid status")
        elif states & (stat + 1):
            raise ValueError("Invalid status")
        elif states & (stat - 2):
            raise ValueError("Invalid status")
        elif states & (stat + 2):
            raise ValueError("Invalid status")
        return states | (stat - 1)

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
        if states & (stat - 1):
            raise ValueError("Invalid status")
        elif states & (stat + 1):
            raise ValueError("Invalid status")
        elif states & (stat - 2):
            raise ValueError("Invalid status")
        elif states & (stat + 2):
            raise ValueError("Invalid status")
        return states | (stat - 1)

    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,if not,raise ValueError.
        :param args: Parameters to be checked,list.
        :return: None.
        """
        if not args or len(args) < 2 or args[0] not in [2, 4]:
            raise ValueError("Parameters must be greater than or equal to 0 and even.")