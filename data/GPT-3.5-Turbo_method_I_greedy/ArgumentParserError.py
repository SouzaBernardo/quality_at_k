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
        args = command_string.split()
        missing_args = set()
    
        for i in range(len(args)):
            arg = args[i]
            if arg.startswith("--"):
                key, value = arg[2:].split("=")
                self.arguments[key] = self._convert_type(value, self.types.get(key))
            elif arg.startswith("-"):
                key = arg[1:]
                self.arguments[key] = True
    
        for req_arg in self.required:
            if req_arg not in self.arguments:
                missing_args.add(req_arg)
    
        if missing_args:
            return False, missing_args
        else:
            return True, None
    

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        return self.arguments.get(key)
    

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it will be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type:str, Argument type, default is str
        >>> parser.add_argument('arg1', True, 'int')
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'int'}
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)
    

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        """
        if value is None:
            return value
        
        arg_type = self.types.get(arg)
        if arg_type == int:
            try:
                return int(value)
            except ValueError:
                return value
        elif arg_type == float:
            try:
                return float(value)
            except ValueError:
                return value
        elif arg_type == bool:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            else:
                return value
        else:
            return value