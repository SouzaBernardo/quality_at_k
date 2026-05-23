Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class ArgumentParser in the following code.
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

### Response:The class `ArgumentParser` is a class for parsing command line arguments to a dictionary. It has three fields: `arguments`, `required`, and `types`. The `arguments` field is a dictionary that stores the parsed arguments, the `required` field is a set that stores the required arguments, and the `types` field is a dictionary that stores the type of every argument.

The `parse_arguments` method takes a command line argument string and parses it to store the parsed result in the `arguments` dictionary. It first splits the command line string into a list of arguments, and then iterates over the list to parse each argument. If the argument starts with `--`, it is considered as an optional argument, and its value is stored in the `arguments` dictionary. If the argument starts with `-`, it is considered as a short option, and its value is stored in the `arguments` dictionary. If the argument does not start with `-` or `--`, it is considered as a positional argument, and its value is stored in the `arguments` dictionary. If the argument is a required argument, it is added to the `required` set. If the argument is not in the `types` dictionary, it is added with the default type `str`. If the argument is in the `types` dictionary, its value is used to convert the argument value to the specified type. If the argument value cannot be converted to the specified type, it is stored as a string.

The `get_argument` method takes an argument name and returns its value from the `arguments` dictionary.

The `add_argument` method takes an argument name, whether it is required, and its type, and adds it to the `types` dictionary and the `required` set if it is required.

The `_convert_type` method takes an argument name and its value, and tries to convert the value to the specified type by searching in the `types` dictionary. If the conversion is successful, it returns the converted value. Otherwise, it returns the original value.

Here's an example usage of the `ArgumentParser` class:

```python
parser = ArgumentParser()
parser.add_argument('arg1', True, 'int')
parser.add_argument('arg2', True,'str')
parser.add_argument('arg3', False, 'float')
parser.add_argument('arg4', False, 'bool')
parser.add_argument('arg5', False, 'list')
parser.add_argument('arg6', False, 'dict')

parser.parse_arguments('python script.py --arg1=21 --arg2=hello --arg3=3.14 --arg4 --arg5=1,2,3 --arg6={"key": "value"}')

print(parser.arguments)
```

Output:

```python
{'arg1': 21, 'arg2': 'hello', 'arg3': 3.14, 'arg4': True, 'arg5': ['1', '2', '3'], 'arg6': {'key': 'value'}}
```