import re
class RegexUtils: 




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
        return self.findall(pattern, text)



    def split(self, pattern, text):
        return self.split(r'\b' + pattern + '\b', text)

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :param pattern: string, Regular expression pattern
        :param replacement: Text to replace with
        :param text: string, Text to be replaced
        :return: string, Text after replacement
        
        Replace the substring matched by a regular expression with the specified string
        
        Replace the substring matched by a regular expression with the specified string
        
        Replace the substring matched by a regular expression with the specified string
        
        Replace the substring matched by a regular expression with the specified string
        """
        match = re.search(pattern, text)
        if match:
            return text.replace(match.group(0), replacement)
        else:
            return text

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        """
        email_patterns = []
        for email_address in self.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'):
            email_patterns.append(r'\b{}\b'.format(email_address))
        return r'\b{}\b'.format(email_patterns)



    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
       'newsletter@example.com'
        """
        return [
            r'[.!?][\s]{1,2}(?=[A-Z])',
            r'\s+',
        ]



    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :param phone_number: Phone number to be verified
        :return: True or False, indicating whether the phone number is valid
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """
        pattern = f"^((\d{3}-\d{3}-\d{4})|(\d{3}-\d{3}-\d{5})|(\d{3}-\d{4}-\d{6})|(\d{4}-\d{5}-\d{6})|(\d{4}-\d{5}-\d{7})|(\d{5}-\d{6}-\d{7})|(\d{6}-\d{7}-\d{8})|(\d{7}-\d{8}-\d{9}))$"
        if re.match(pattern, phone_number):
            return True
        else:
            return False

