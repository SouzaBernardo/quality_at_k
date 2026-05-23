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
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path.segments
        ['foo', 'bar']
        """


    def __repr__(self):
        """
        Returns a string representation of the UrlPath object.
        :return: str, the string representation of the UrlPath object.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path.segments
        ['foo', 'bar']
        """


    def __len__(self):
        """
        Returns the number of segments in the UrlPath object.
        :return: int, the number of segments in the UrlPath object.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path.segments
        2
        """


    def __getitem__(self, index):
        """
        Returns the segment at the given index in the UrlPath object.
        :param index: int, the index of the segment to return.
        :return: str, the segment at the given index in the UrlPath object.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path[0]
        'foo'
        >>> url_path[1]
        'bar'
        """


    def __setitem__(self, index, value):
        """
        Sets the segment at the given index in the UrlPath object.
        :param index: int, the index of the segment to set.
        :param value: str, the segment to set.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path[0] = 'foo'
        >>> url_path[1] = 'bar'
        >>> url_path[0]
        'foo'
        >>> url_path[1]
        'bar'
        """


    def __delitem__(self, index):
        """
        Deletes the segment at the given index in the UrlPath object.
        :param index: int, the index of the segment to delete.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path[0]
        'foo'
        >>> url_path[1]
        'bar'
        >>> url_path.delitem(0)
        >>> url_path[0]
        ''
        """


    def __iter__(self):
        """
        Returns an iterator over the segments in the UrlPath object.
        :return: an iterator over the segments in the UrlPath object.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path[0]
        'foo'
        >>> url_path[1]
        'bar'
        >>> url_path.iter()
        [('foo', 'bar')]
        """


    def __contains__(self, value):
        """
        Returns whether the given value is in the UrlPath object.
        :param value: str, the value to check.
        :return: bool, whether the given value is in the UrlPath object.
        >>> url_path = UrlPath()
        >>> url_path.segments = ['foo', 'bar']
        >>> url_path[0]
        'foo'
        >>> url_path[1]
        'bar'
        >>> url_path.contains('foo')
        True
        >>> url_path.contains('bar')
        False
        """