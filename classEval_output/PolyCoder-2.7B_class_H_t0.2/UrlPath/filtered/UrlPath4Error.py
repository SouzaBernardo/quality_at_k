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


    def build_path(self, path, encoding):
        """
        Builds the given path string by adding the given encoding to the segments.
        :param path: str, the path string to build.
        :param encoding: str, the encoding to use for the path string.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.build_path('/foo/bar/', 'utf-8')
        '/foo/bar/'

        """


    def __str__(self):
        """
        Returns a string representation of the UrlPath object.
        """
        return str(self.segments)


    def __repr__(self):
        """
        Returns a string representation of the UrlPath object.
        """
        return str(self.segments)


    def __len__(self):
        """
        Returns the number of segments in the UrlPath object.
        """
        return len(self.segments)


    def __getitem__(self, index):
        """
        Returns the segment at the given index.
        :param index: int, the index of the segment to return.
        :return: str, the segment at the given index.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')
        >>> url_path[0]
        'foo'
        >>> url_path[1]
        'bar'
        >>> url_path[2]
        ''
        >>> url_path[3]
        ''
        >>> url_path[4]
        'foo'
        >>> url_path[5]
        'bar'
        >>> url_path[6]
        ''
        >>> url_path[7]
        ''
        >>> url_path[8]
        ''
        >>> url_path[9]
        ''
        >>> url_path[10]
        ''
        >>> url_path[11]
        ''
        >>> url_path[12]
        ''
        >>> url_path[13]
        ''
        >>> url_path[14]
        ''
        >>> url_path[15]
        ''
        >>> url_path[16]
        ''
        >>> url_path[17]
        ''
        >>> url_path[18]
        ''
        >>> url_path[19]
        ''
        >>> url_path[20]
        ''
        >>> url_path[21]
        ''
        >>> url_path[22]
        ''
        >>> url_path[23]
        ''
        >>> url_path[24]
        ''
        >>> url_path[25]
        ''
        >>> url_path[26]
        ''
        >>> url_path[27]
        ''
        >>> url_path[28]
        ''
        >>> url_path[29]
        ''
        >>> url_path[30]
        ''
        >>> url_path[31]
        ''
        >>> url_path[32]
        ''
        >>> url_path[33]
        ''
        >>> url_path[34]
        ''
        >>> url_path[35]
        ''
        >>> url_path[36]
        ''
        >>> url_path[37]
        ''
        >>> url_path[38]
        ''
        >>> url