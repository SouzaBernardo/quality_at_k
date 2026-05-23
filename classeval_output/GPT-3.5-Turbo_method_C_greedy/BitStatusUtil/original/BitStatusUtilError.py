
class BitStatusUtil: 


    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        """
        return states | stat
    

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: True if the current status contains the specified status, otherwise False, bool.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise ValueError("Both 'states' and 'stat' parameters must be integers.")
        
        return (states & stat) == stat
    

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: The status after removing the specified status, int.
        """
        if isinstance(states, int) and isinstance(stat, int):
            return states & ~stat
        else:
            raise ValueError("Invalid parameters. Both 'states' and 'stat' should be integers.")
    

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even, if not, raise ValueError.
        :param args: Parameters to be checked, list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 not even
        """
        for arg in args:
            if arg < 0 or arg % 2 != 0:
                raise ValueError(f"{arg} not even")
    