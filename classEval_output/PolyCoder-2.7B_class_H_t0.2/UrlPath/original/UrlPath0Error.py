import urllib.parse

class UrlPath:
    """
    The  class is a utility for encapsulating and manipulating the path component of a URL, including adding nodes, parsing path strings, and building path strings with optional encoding.
    """

    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        """
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def parse(self, path, charset):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """


    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'

        """


    def __str__(self):
        """
        Returns a string representation of the UrlPath object.
        :return: str, the string representation of the UrlPath object.
        """


    def __repr__(self):
        """
        Returns a string representation of the UrlPath object.
        :return: str, the string representation of the UrlPath object.
        """


    def __len__(self):
        """
        Returns the number of segments in the UrlPath object.
        :return: int, the number of segments in the UrlPath object.
        """


    def __getitem__(self, index):
        """
        Returns the segment at the given index in the UrlPath object.
        :param index: int, the index of the segment to return.
        :return: str, the segment at the given index in the UrlPath object.
        """


    def __setitem__(self, index, value):
        """
        Sets the segment at the given index in the UrlPath object.
        :param index: int, the index of the segment to set.
        :param value: str, the segment to set.
        """


    def __add__(self, value):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param value: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __add__(self, value):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param value: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __iadd__(self, value):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param value: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __iadd__(self, value):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param value: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __sub__(self, value):
        """
        Subtracts a segment from the list of segments in the UrlPath.
        :param value: str, the segment to subtract.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __sub__(self, value):
        """
        Subtracts a segment from the list of segments in the UrlPath.
        :param value: str, the segment to subtract.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __mul__(self, value):
        """
        Multiplies a segment from the list of segments in the UrlPath.
        :param value: str, the segment to multiply.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """


    def __mul__(self, value):
        """
        Multiplies a