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


    def build(self, path, charset):
        """
        Builds the given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        >>> url_path = UrlPath()
        >>> url_path.build('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """


    def __str__(self):
        """
        Returns a string representation of the UrlPath object.
        """


    def __repr__(self):
        """
        Returns a string representation of the UrlPath object.
        """


    def __len__(self):
        """
        Returns the number of segments in the UrlPath.
        """


    def __getitem__(self, index):
        """
        Returns the segment at the given index.
        :param index: int, the index of the segment to return.
        :return: str, the segment at the given index.
        """


    def __setitem__(self, index, value):
        """
        Sets the segment at the given index.
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
        >>> url_path.add('baz')
        >>> url_path.add('qux')
        >>> url_path.add('quux')
        >>> url_path.add('quuz')
        >>> url_path.add('quuze')
        >>> url_path.add('quuze2')
        >>> url_path.add('quuze3')
        >>> url_path.add('quuze4')
        >>> url_path.add('quuze5')
        >>> url_path.add('quuze6')
        >>> url_path.add('quuze7')
        >>> url_path.add('quuze8')
        >>> url_path.add('quuze9')
        >>> url_path.add('quuze10')
        >>> url_path.add('quuze11')
        >>> url_path.add('quuze12')
        >>> url_path.add('quuze13')
        >>> url_path.add('quuze14')
        >>> url_path.add('quuze15')
        >>> url_path.add('quuze16')
        >>> url_path.add('quuze17')
        >>> url_path.add('quuze18')
        >>> url_path.add('quuze19')
        >>> url_path.add('quuze20')
        >>> url_path.add('quuze21')
        >>> url_path.add('quuze22')
        >>> url_path.add('quuze23')
        >>> url_path.add('quuze24')
        >>> url_path.add('quuze25')
        >>> url_path.add('quuze26')
        >>> url_path.add('quuze27')
        >>> url_path.add('quuze28')
        >>> url_path.add('quuze29')
        >>> url_path.add('quuze30')
        >>> url_path.add('quuze31')
        >>> url_path.add('quuze32')
        >>> url_path.add('quuze33')
        >>> url_path.add('quuze34')
        >>> url_path.add('quuze35')
        >>> url_path.add('quuze36')
        >>> url_path.add('quuze37')
        >>> url_path.add('quuze38')
        >>> url_path.add('quuze39