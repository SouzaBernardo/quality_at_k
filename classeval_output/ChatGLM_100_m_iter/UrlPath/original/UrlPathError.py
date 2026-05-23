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
        if segment in self.segments:
            self.segments.append(segment)
        else:
            self.with_end_tag = True

    def parse(self, path, charset):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        """
        if not path.startswith('/'):
            path = path + '/'
        path = urllib.parse.urlparse(path, self.with_end_tag)
        segments = []
        for part in path.split('/'):
            if part == '':
                continue
            segments.append(part)
        if charset:
            segments = [segment.decode(charset) for segment in segments]
        return self.segments

    def fix_path(self, path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        if path.startswith('/'):
            path = path[1:]
        path = urllib.parse.urlparse(path, self.with_end_tag)
        return path.replace('/', '').replace('//', '')