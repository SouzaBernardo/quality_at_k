import re
class RegexUtils: 

    def match(self, pattern, text):
        """
        Check if the text matches the regular expression
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: True or False, representing whether the text matches the regular expression or not
        """
        return bool(re.match(pattern, text))
    def findall(self, pattern, text):
        return re.findall(pattern, text)
    def split(self, pattern, text):
        return re.split(pattern, text)
    def sub(self, pattern, replacement, text):
        return re.sub(pattern, replacement, text)
    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        """
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        """
        return r'\b\d{3}-\d{3}-\d{4}\b'
    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        """
        return '[.!?][\s]{1,2}(?=[A-Z])'
    
    def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        """
        sentences = re.split('(?<=[.!?]) +', text)
        sentences = [s.rstrip('.!?') for s in sentences[:-1]] + [sentences[-1]]
        return sentences

    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :param phone_number: Phone number to be verified
        :return: True or False, indicating whether the phone number is valid
        """
        phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
        if phone_number_pattern.match(phone_number):
            return True
        else:
            return False
    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :param text: string, input text
        :return: list of string, All extracted email addresses
        """
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, text)
