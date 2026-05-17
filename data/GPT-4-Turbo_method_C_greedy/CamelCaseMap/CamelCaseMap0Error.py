class CamelCaseMap: 
    def __init__(self):
        """
        Initialize data to an empty dictionary
        """
        self._data = {}


    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :param key:str
        :return:str,the value corresponding to the key
        """
        camel_key = self._to_camel_case(key)
        if camel_key in self._data:
            return self._data[camel_key]
        else:
            raise KeyError(f"Key '{key}' not found in CamelCaseMap.")
    
    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key:str
        :param value:str, the specified value
        :return:None
        """
        camel_case_key = self._to_camel_case(key)
        self._data[camel_case_key] = value
    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key:str
        :return:None
        """
        camel_key = self._to_camel_case(key)
        if camel_key in self._data:
            del self._data[camel_key]
        else:
            raise KeyError(f"Key '{key}' not found in the dictionary.")
    def __iter__(self):
        """
        Returns an iterator over the keys of the dictionary
        """
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def _convert_key(self, key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        """
        parts = key.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    @staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        """
        components = key.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])