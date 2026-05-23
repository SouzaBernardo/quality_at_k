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
        """
        # Split the text into a list of words
        words = text.split()

        # Check if each word matches the pattern
        for word in words:
            if re.match(pattern, word):
                return True

        return False

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: list of string, List of all matching substrings
        >>> ru = RegexUtils()
        >>> ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['123-456-7890', '876-286-9876', '987-762-9767']
        """
        # Split the text into a list of words
        words = text.split()

        # Check if each word matches the pattern
        for word in words:
            if re.match(pattern, word):
                # Add the word to the list of matching substrings
                match = [word]
                for sub in word.split():
                    if sub.isdigit():
                        match.append(sub)
                return match

        return []

    def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to be split
        :return: list of string, List of substrings after splitting
        """
        # Split the text into a list of words
        words = text.split()

        # Check if each word matches the pattern
        for word in words:
            if re.match(pattern, word):
                # Add the word to the list of matching substrings
                match = [word]
                for sub in word.split():
                    if sub.isdigit():
                        match.append(sub)
                return match

        return []

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :param pattern: string, Regular expression pattern
        :param replacement: Text to replace with
        :param text: string, Text to be replaced
        :return: string, Text after replacement
        """
        # Replace the substring matched by the regular expression with the specified string
        text = re.sub(pattern, replacement, text)
        return text

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        """

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        """
        # Define predefined patterns for validating phone numbers
        patterns = [
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})$',
            r'^(\d{3}-\d{3}-\d{4})(\d{3}-\d{3}-\d{4})(\d{







