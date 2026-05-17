
class ArgumentParser:  
    """
    This is a class for parsing command line arguments to a dictionary.
    """

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
        # Check for missing required arguments
        missing_args = set()
        for arg in command_string.split():
            if arg.startswith("--"):
                missing_args.add(arg)
                continue
            if arg.startswith("-"):
                if arg in self.required:
                    missing_args.add(arg)
                else:
                    return (False, missing_args)
            else:
                return (False, missing_args)

        # Parse the arguments
        for arg in command_string.split():
            if arg.startswith("--"):
                self.arguments[arg] = True
                continue
            if arg.startswith("-"):
                self.arguments[arg] = False
                continue
            if arg.startswith("--"):
                if arg in self.required:
                    self.arguments[arg] = True
                else:
                    return (False, missing_args)
            else:
                if arg in self.required:
                    self.arguments[arg] = True
                else:
                    return (False, missing_args)

        # Check for missing required types
        missing_types = set()
        for arg in self.arguments.keys():
            if arg in self.types:
                missing_types.add(arg)
                continue
            if arg.startswith("--"):
                if arg in self.required:
                    self.types[arg] = True
                else:
                    return (False, missing_types)
            else:
                return (False, missing_types)

        # Parse the types
        for arg in self.arguments.keys():
            if arg in self.types:
                self.types[arg] = True
                continue
            if arg.startswith("--"):
                if arg in self.required:
                    self.types[arg] = True
                else:
                    return (False, missing_types)
            else:
                return (False, missing_types)

        return (True, missing_args)




    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
        if key not in self.arguments:
            return None
        return self.arguments[key]





    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it wull be added to the required set.
        """

        """