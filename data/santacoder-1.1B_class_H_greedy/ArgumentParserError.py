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

    def _check_required(self, arg):
        """
        Check if the argument is required.
        :param arg: str, argument name
        :return: True if the argument is required, False otherwise
        >>> parser.required
        {'arg1'}
        >>> parser._check_required('arg1')
        True
        >>> parser._check_required('arg2')
        False
        """

    def _check_type(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_type('arg1', '21')
        True
        >>> parser._check_type('arg1', '2.1')
        False
        """

    def _check_value(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value('arg1', '21')
        True
        >>> parser._check_value('arg1', '2.1')
        False
        """

    def _check_value_range(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_range('arg1', '21')
        True
        >>> parser._check_value_range('arg1', '2.1')
        False
        """

    def _check_value_list(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_list('arg1', '21')
        True
        >>> parser._check_value_list('arg1', '2.1')
        False
        """

    def _check_value_dict(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_dict('arg1', '21')
        True
        >>> parser._check_value_dict('arg1', '2.1')
        False
        """

    def _check_value_bool(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_bool('arg1', '21')
        True
        >>> parser._check_value_bool('arg1', '2.1')
        False
        """

    def _check_value_file(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_file('arg1', '21')
        True
        >>> parser._check_value_file('arg1', '2.1')
        False
        """

    def _check_value_dir(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_dir('arg1', '21')
        True
        >>> parser._check_value_dir('arg1', '2.1')
        False
        """

    def _check_value_path(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_path('arg1', '21')
        True
        >>> parser._check_value_path('arg1', '2.1')
        False
        """

    def _check_value_url(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True if the argument is of the specified type, False otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._check_value_url('arg1', '21')
        True
        >>> parser._check_value_url('arg1', '2.1')
        False
        """

    def _check_value_email(self, arg, value):
        """
        Check if the argument is of the specified type.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: True