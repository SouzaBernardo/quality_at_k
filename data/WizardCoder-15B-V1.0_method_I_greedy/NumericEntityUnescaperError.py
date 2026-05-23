class NumericEntityUnescaper:  
    """
    This is a class that provides functionality to replace numeric entities with their corresponding characters in a given string.
    """

    def __init__(self):
        pass



    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        """
        # Define a regular expression pattern to match numeric character references
        pattern = r'&#([0-9]+);'
        # Use the re.sub() method to replace all occurrences of the pattern with the corresponding Unicode characters
        return re.sub(pattern, lambda match: chr(int(match.group(1))), string)