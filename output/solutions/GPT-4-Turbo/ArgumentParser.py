class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split()[2:]  # remove "python script.py"
        missing_args = self.required.copy()
        for arg in args:
            if "=" in arg:  # --arg=value
                key, value = arg.split("=")
                key = key.lstrip("-")
                value = self._convert_type(key, value)
                self.arguments[key] = value
                if key in missing_args:
                    missing_args.remove(key)
            else:  # -arg or --option
                key = arg.lstrip("-")
                if key in self.types:
                    self.arguments[key] = None
                else:
                    self.arguments[key] = True
                if key in missing_args:
                    missing_args.remove(key)
        if missing_args:
            return False, missing_args
        else:
            return True, None

    def get_argument(self, key):
        return self.arguments.get(key, None)

    def add_argument(self, arg, required=False, arg_type=str):
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        arg_type = self.types.get(arg, str)
        try:
            return arg_type(value)
        except ValueError:
            return value