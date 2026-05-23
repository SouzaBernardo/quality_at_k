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
        # Decode the path string using the specified character encoding
        decoded_path = urllib.parse.unquote_plus(path, encoding=charset)
        # Split the decoded path string into segments
        segments = urllib.parse.urlsplit(decoded_path).path.strip('/').split('/')
        # Add the segments to the list of segments in the UrlPath object
        for segment in segments:
            self.segments.append(segment)
        # Check if the last segment of the path string is an end tag
        if segments[-1] == '':
            self.with_end_tag = True

    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        return path.strip('/')