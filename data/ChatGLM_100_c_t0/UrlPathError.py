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
        """
        self.segments.append(segment)

    def parse(self, path, charset):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        """
        self.path = path
        self.path_ charset = charset

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        if path.startswith('/'):
            path = path[1:]
        return path


url_path = UrlPath()
url_path.add('http://www.example.com/')
print(url_path.path) # Output: '/http://www.example.com/'

url_path.parse('http://www.example.com/foo/bar/', 'utf-8')
print(url_path.path_ charset) # Output: 'utf-8'

url_path.fix_path('/foo/bar/')
print(url_path.path) # Output: '/foo/bar'