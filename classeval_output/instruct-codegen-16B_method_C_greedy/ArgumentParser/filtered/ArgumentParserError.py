class ArgumentParser: 
    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.requried is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
        >>> parser.arguments
        {'key1': 'value1', 'option1': True}
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'type1'}
        """
        self.arguments = {}
        self.required = set()
        self.types = {}



    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
        # split the command string
        args = command_string.split()
        # check for required arguments
        missing_args = set()
        for arg in self.required:
            if arg not in args:
                missing_args.add(arg)
        # if there are missing required arguments, return False
        if len(missing_args) > 0:
            return (False, missing_args)
        # parse the arguments
        for arg in args:
            # check if the argument is required
            if arg in self.required:
                self.arguments[arg] = self._convert_type(arg, args[args.index(arg)+1])
            # parse the argument types
            else:
                self.arguments[arg] = self._convert_type(arg, args[args.index(arg)+1])
        return (True, None)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        if key in self.arguments:
            return self.arguments[key]
        else:
            return None



    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            return value