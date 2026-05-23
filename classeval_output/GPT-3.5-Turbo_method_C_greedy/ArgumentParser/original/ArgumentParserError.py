
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
        Parses the given command line argument string and invokes _convert_type to store the parsed result in specific types in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        """
        missing_args = set(self.required)  # Initialize missing_args with all required arguments
        args = command_string.split()  # Split the command_string into individual arguments
    
        # Iterate over the arguments
        for i in range(len(args)):
            arg = args[i]
    
            # Check if the argument starts with '--' or '-'
            if arg.startswith('--'):
                # Argument in the format '--arg=value'
                arg_name, arg_value = arg[2:].split('=')
                self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                if arg_name in missing_args:
                    missing_args.remove(arg_name)
            elif arg.startswith('-'):
                # Argument in the format '-arg value'
                arg_name = arg[1:]
                arg_value = args[i+1]
                self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                if arg_name in missing_args:
                    missing_args.remove(arg_name)
    
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
        if arg in self.types:
            try:
                return self.types[arg](value)
            except ValueError:
                return value
        else:
            return value
    