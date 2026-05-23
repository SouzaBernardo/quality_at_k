import unittest
class BitStatusUtil: 


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
        :return: True if the current status contains the specified status, otherwise False,bool.
        """
        if stat in states:
            return True
        for i in range(len(states)):
            if states[i]!= stat:
                return False
        return False

    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(6,2)
        6
        >>> bit_status_util.add(6,3)
        10
        >>> bit_status_util.add(6,4)
        14
        >>> bit_status_util.add(6,5)
        18
        >>> bit_status_util.add(6,6)
        22
        >>> bit_status_util.has(6,2)
        True
        >>> bit_status_util.has(6,3)
        True
        >>> bit_status_util.has(6,4)
        True
        >>> bit_status_util.has(6,5)
        True
        >>> bit_status_util.has(6,6)
        True
        >>> bit_status_util.check(6)
        True
        >>> bit_status_util.remove(6,2)
        4
        """
        pass


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
        if not args or len(args)!= 2 or not any(int(x) % 2 for x in args):
            raise ValueError("args must be greater than or equal to 0 and are even")
        return None