class CamelCaseMap: 
    def __init__(self):
        """
        Initialize data to an empty dictionary
        """
        self._data = {}



    def __getitem__(self, key):
        converted_key = self._convert_key(key)
        return self._data[converted_key]
    

    def __setitem__(self, key, value):
        converted_key = self._convert_key(key)
        self._data[converted_key] = value
    

    def __delitem__(self, key):
        converted_key = self._convert_key(key)
        del self._data[converted_key]
    

    def __iter__(self):
        return iter(self._data)
    

    def __len__(self):
        """
        Returns the length of the own data
        :return: int, length of data
        """
        return len(self._data)
    

    def _convert_key(self, key):
        """
        Convert key string into camel case
        :param key: str
        :return: str, converted key string
        """
        words = key.split('_')
        camel_case_key = words[0] + ''.join(word.title() for word in words[1:])
        return camel_case_key
    

    @staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
        words = key.split('_')
        camel_case_key = words[0] + ''.join(word.title() for word in words[1:])
        return camel_case_key