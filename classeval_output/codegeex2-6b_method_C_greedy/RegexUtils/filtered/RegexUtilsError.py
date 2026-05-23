import re
class RegexUtils: 











    def sub(self, pattern, replacement, text):


    def generate_email_pattern(self):
        
        return '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


    def generate_phone_number_pattern(self):
        
        return '\b\d{3}-\d{3}-\d{4}\b'


    def generate_split_sentences_pattern(self):
        
        return '[.!?][\s]{1,2}(?=[A-Z])'





    def validate_phone_number(self, phone_number):


    def extract_email(self, text):