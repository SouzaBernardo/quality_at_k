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
        if path.startswith('/'):
            path = path[1:]

        if path.endswith('/'):
            path = path[:-1]

        return path


    def parse_path(self, path):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.parse_path('/foo/bar/')
        'foo/bar'
        >>> url_path.parse_path('/foo/bar/baz/')
        'foo/bar/baz'
        >>> url_path.parse_path('/foo/bar/baz/')
        'foo/bar/baz'
        """

        if path.startswith('/'):
            path = path[1:]

        if path.endswith('/'):
            path = path[:-1]

        return path


    def parse_url(self, url):
        """
        Parses a given URL and populates the list of segments in the UrlPath.
        :param url: str, the URL to parse.
        :return: str, the fixed URL.
        >>> url_path = UrlPath()
        >>> url_path.parse_url('http://example.com/foo/bar/baz')
        'http://example.com/foo/bar/baz'
        >>> url_path.parse_url('http://example.com/foo/bar/baz/')
        'http://example.com/foo/bar/baz'
        >>> url_path.parse_url('http://example.com/foo/bar/baz/')
        'http://example.com/foo/bar/baz'
        """

        if url.startswith('/'):
            url = url[1:]

        if url.endswith('/'):
            url = url[:-1]

        return url


    def parse_path_url(self, path, url):
        """
        Parses a given path and URL and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param url: str, the URL to parse.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.parse_path_url('/foo/bar/baz', 'http://example.com/foo/bar/baz')
        'foo/bar/baz'
        >>> url_path.parse_path_url('/foo/bar/baz', 'http://example.com/foo/bar/baz/')
        'foo/bar/baz'
        >>> url_path.parse_path_url('/foo/bar/baz', 'http://example.com/foo/bar/baz/')
        'foo/bar/baz'
        """

        if path.startswith('/'):
            path = path[1:]

        if path.endswith('/'):
            path = path[:-1]

        if url.startswith('/'):
            url = url[1:]

        if url.endswith('/'):
            url = url[:-1]

        return path, url


    def parse_path_url_with_params(self, path, url, params):
        """
        Parses a given path and URL and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param url: str, the URL to parse.
        :param params: dict, the parameters to parse.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.parse_path_url_with_params('/foo/bar/baz', 'http://example.com/foo/bar/baz', {'foo': 'bar'})
        'foo/bar/baz'
        >>> url_path.parse_path_url_with_params('/foo/bar/baz', 'http://example.com/foo/bar/baz/')
        'foo/bar/baz'
       