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
        if not command_string:
            return False, set()
        args = command_string.split()
        if len(args) == 0:
            return False, set()
        if len(args) == 1:
            return True, set()
        required = set()
        for arg in args:
            if arg.startswith('-'):
                required.add(arg[1:])
            else:
                required.add(arg)
        missing_args = set()
        for arg in args:
            if arg.startswith('--'):
                if arg.startswith('--') and arg.endswith('--'):
                    missing_args.add(arg[2:])
                else:
                    missing_args.add(arg)
            else:
                missing_args.add(arg)
        if missing_args:
            return False, missing_args
        return True, required


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
        if not required:
            self.required.add(arg)
            return
        if arg_type =='str':
            self.types[arg] = arg_type
            return
        if arg_type == 'int':
            self.types[arg] = 'int'
            return
        if arg_type == 'bool':
            self.types[arg] = 'bool'
            return
        if arg_type == 'float':
            self.types[arg] = 'float'
            return
        if arg_type == 'list':
            self.types[arg] = 'list'
            return
        if arg_type == 'dict':
            self.types[arg] = 'dict'
            return
        if arg_type == 'file':
            self.types[arg] = 'file'
            return
        if arg_type == 'dir':
            self.types[arg] = 'dir'
            return
        if arg_type == 'path':
            self.types[arg] = 'path'
            return
        if arg_type =='strlist':
            self.types[arg] ='strlist'
            return
        if arg_type =='strdict':
            self.types[arg] ='strdict'
            return
        if arg_type =='str':
            self.types[arg] ='str'
            return
        if arg_type == 'boollist':
            self.types[arg] = 'boollist'
            return
        if arg_type == 'booldict':
            self.types[arg] = 'booldict'
            return
        if arg_type == 'bool':
            self.types[arg] = 'bool'
            return
        if arg_type == 'floatlist':
            self.types[arg] = 'floatlist'
            return
        if arg_type == 'floatdict':
            self.types[arg] = 'floatdict'
            return
        if arg_type == 'float':
            self.types[arg] = 'float'
            return
        if arg_type == 'listlist':
            self.types[arg] = 'listlist'
            return
        if arg_type == 'listdict':
            self.types[arg] = 'listdict'
            return
        if arg_type == 'list':
            self.types[arg] = 'list'
            return
        if arg_type == 'dictlist':
            self.types[arg] = 'dictlist'
            return
        if arg_type == 'dictdict':
            self.types[arg] = 'dictdict'
            return
        if arg_type == 'dict':
            self.types[arg] = 'dict'
            return
        if arg_type == 'filelist':
            self.types[arg] = 'filelist'
            return
        if arg_type == 'filedict':
            self.types[arg] = 'filedict'
            return
        if arg_type == 'file':
            self.types[arg] = 'file'
     

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
        if value in self.types:
            return self.types[value]
        else:
            return value