
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
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("The states and stat parameters should be of type int.")
        if states < 0 or stat < 0:
            raise ValueError("The states and stat parameters should be non-negative.")
        return states | stat

    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("The states and stat parameters should be of type int.")
        if states < 0 or stat < 0:
            raise ValueError("The states and stat parameters should be non-negative.")
        return (states & stat)!= 0

    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("The states and stat parameters should be of type int.")
        if states < 0 or stat < 0:
            raise ValueError("The states and stat parameters should be non-negative.")
        return states & ~stat

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
        if any(x % 2!= 0 for x in args):
            raise ValueError("args should contain only even numbers.")
        if any(x < 0 for x in args):
            raise ValueError("args should contain only non-negative numbers.")