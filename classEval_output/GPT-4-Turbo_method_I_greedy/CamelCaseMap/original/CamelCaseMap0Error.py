
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
        camel_case_key = ''.join(word.title() for word in key.split('_'))
        return self._data.get(camel_case_key)
    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key:str
        :param value:str, the specified value
        :return:None
        """
        camel_case_key = ''.join(word.title() for word in key.split('_'))
        self._data[camel_case_key] = value
    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key:str
        :return:None
        """
        camel_case_key = ''.join(word.title() for word in key.split('_'))
        if camel_case_key in self._data:
            del self._data[camel_case_key]
    
    def __iter__(self):
        """
        Return an iterator over the keys of the dictionary
        :return: Iterator
        """
        return iter(self._data)
    def __len__(self):
        """
        Returns the length of the own data
        :return:int, length of data
        """
        return len(self._data)
    def _convert_key(self, key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        """
        words = key.split('_')
        return words[0].lower() + ''.join(word.title() for word in words[1:])
    
    @staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        """
        words = key.split('_')
        return words[0].lower() + ''.join(word.title() for word in words[1:])
