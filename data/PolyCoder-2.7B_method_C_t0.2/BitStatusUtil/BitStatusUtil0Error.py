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
        if not isinstance(stat, int):
            raise TypeError("stat must be an int")
        if not isinstance(states, int):
            raise TypeError("states must be an int")
        if not isinstance(stat, int):
            raise TypeError("stat must be an int")
        if stat < 0:
            raise ValueError("stat must be >= 0")
        if states < 0:
            raise ValueError("states must be >= 0")
        if stat > states:
            raise ValueError("stat must be <= states")
        if stat == states:
            return stat
        if states == 0:
            return states
        if states == 1:
            return stat
        if states == 2:
            return stat | 1
        if states == 3:
            return stat | 2
        if states == 4:
            return stat | 4
        if states == 5:
            return stat | 8
        if states == 6:
            return stat | 16
        if states == 7:
            return stat | 32
        if states == 8:
            return stat | 64
        if states == 9:
            return stat | 128
        if states == 10:
            return stat | 256
        if states == 11:
            return stat | 512
        if states == 12:
            return stat | 1024
        if states == 13:
            return stat | 2048
        if states == 14:
            return stat | 4096
        if states == 15:
            return stat | 8192
        if states == 16:
            return stat | 16384
        if states == 17:
            return stat | 32768
        if states == 18:
            return stat | 65536
        if states == 19:
            return stat | 131072
        if states == 20:
            return stat | 262144
        if states == 21:
            return stat | 524288
        if states == 22:
            return stat | 1048576
        if states == 23:
            return stat | 2097152
        if states == 24:
            return stat | 4194304
        if states == 25:
            return stat | 8388608
        if states == 26:
            return stat | 16777216
        if states == 27:
            return stat | 33554432
        if states == 28:
            return stat | 67108864
        if states == 29:
            return stat | 134217728
        if states == 30:
            return stat | 268435456
        if states == 31:
            return stat | 536870912
        if states == 32:
            return stat | 1073741824
        if states == 33:
            return stat | 2147483648
        if states == 34:
            return stat | 0
        if states == 35:
            return stat | 1
        if states == 36:
            return stat | 2
        if states == 37:
            return stat | 4
        if states == 38:
            return stat | 8
        if states == 39:
            return stat | 16
        if states == 40:
            return stat | 32
        if states == 41:
            return stat | 64
        if states == 42:
            return stat | 128
        if states == 43:
            return stat | 256
        if states == 44:
            return stat | 512
        if states == 45:
            return stat | 1024
        if states == 46:
            return stat | 2048
        if states == 47:
            return stat | 4096
        if states == 48:
            return stat | 8192
        if states == 49:
            return stat | 16384
        if states == 50:
            return stat | 32768
        if states == 51:
      

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
        pass