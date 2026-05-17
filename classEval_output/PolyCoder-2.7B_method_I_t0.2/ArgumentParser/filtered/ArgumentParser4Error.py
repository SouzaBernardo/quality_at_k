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
        self.requried = set()
        self.required = set()
        self.types = {}
        for arg in command_string.split():
            if arg.startswith("--"):
                if arg.startswith("--") and len(arg) > 2:
                    self.requried.add(arg[2:])
                    continue
                elif arg.startswith("--") and len(arg) > 1:
                    self.required.add(arg[1:])
                    continue
                else:
                    self.requried.add(arg)
                    continue
            if arg.startswith("-") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.required.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):
                self.requried.add(arg)
                continue
            if arg.startswith("=") or arg.startswith("--"):