import unittest
class BitStatusUtil: 


    def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheether they are legal.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6
        >>> bit_status_util.add(2,5)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "test_BitStatusUtil.py", line 21, in add
            raise ValueError("Invalid input")
        ValueError: Invalid input

    def has(states, stat):
        """
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6,2)
        True
    
        >>> bit_status_util.has(6,3)
        False
        """
        if states >= 8:
            raise ValueError("Invalid status")
        if stat >= 8:
            raise ValueError("Invalid status")
        return states & stat == stat

    def remove(states, stat):
        """
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6,2)
        4
    
        """
        if states < 0 or states > 3 or stat < 0 or stat > 3:
            raise ValueError("Invalid input")
        return (states & ~stat)

    def check(args):
        """
        :param args: Parameters to be checked,list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 not even
        """
        pass