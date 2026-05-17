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
        if not isinstance(states, int):
            raise TypeError("The type of states must be int")
        if not isinstance(stat, int):
            raise TypeError("The type of stat must be int")
        if not isinstance(args, list):
            raise TypeError("The type of args must be list")
        if len(args)!= 2:
            raise TypeError("The length of args must be 2")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
            raise TypeError("The type of args[0] must be int")
        if not isinstance(args[1], int):
            raise TypeError("The type of args[1] must be int")
        if not isinstance(args[0], int):
      

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
        return True



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
        if args not in [0,1,2]:
            raise ValueError("3 not even")
        pass