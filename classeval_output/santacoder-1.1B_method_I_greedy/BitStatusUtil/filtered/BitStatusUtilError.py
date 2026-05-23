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
        if stat < 0 or stat > 255:
            raise ValueError("The status must be between 0 and 255")
        states = states | stat
        return states


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
        if stat < 0 or stat > 255:
            raise ValueError("The status must be between 0 and 255")
        return states & stat == stat



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
        if stat < 0 or stat > 255:
            raise ValueError("The status must be between 0 and 255")
        states = states & ~stat
        return states



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
        if len(args) < 1:
            raise ValueError("The number of parameters must be greater than or equal to 1")
        if len(args) % 2!= 0:
            raise ValueError("The number of parameters must be even")
        for i in range(0, len(args), 2):
            if args[i] < 0 or args[i] > 255:
                raise ValueError("The status must be between 0 and 255")
            if args[i+1] < 0 or args[i+1] > 255:
                raise ValueError("The status must be between 0 and 255")
            if args[i] == args[i+1]:
                raise ValueError("The status must be different")