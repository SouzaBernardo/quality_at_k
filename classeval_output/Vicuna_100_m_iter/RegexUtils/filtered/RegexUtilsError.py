import re
class RegexUtils:  
    """
    The class provides to match, find all occurrences, split, and substitute text using regular expressions. It also includes predefined patterns, validating phone numbers and extracting email addresses.
    """



    def match(self, pattern, text):
        """
        Check if the text matches the regular expression
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: True or False, representing whether the text matches the regular expression or not
        >>> ru = RegexUtils()
        >>> ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
        True

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: list of string, List of all matching substrings
        >>> ru = RegexUtils()
        >>> result = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['123-456-7890', '876-286-9876', '987-762-9767']
        """
        return re.findall(pattern, text)

    def split(self, pattern, text):
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :param pattern: string, Regular expression pattern
        :param replacement: Text to replace with
        :param text: string, Text to be replaced
        :return: string, Text after replacement
        >>> ru = RegexUtils()
        >>> result = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        'phone num abiguygusu phone num kjgufwycs phone num'
        """
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
        return pattern





    def split_sentences(self, text):
        pattern = r'(?<!\p{Punct})(?![ \t\r\n\f])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])(?![.\w])