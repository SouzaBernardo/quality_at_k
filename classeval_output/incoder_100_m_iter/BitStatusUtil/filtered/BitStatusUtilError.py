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
        status = states | stat
        if status < 0 or status > 2**len(states):
            raise ValueError("The status is not legal")
        return status