
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
        output = ""
        i = 0
        while i < len(string):
            if string[i] == '&' and (i+1) < len(string):
                if string[i+1] == '#':
                    output += chr(int(string[i+2 : i+6]))
                    i += 6
                    continue
                else:
                    output += string[i]
                    i += 1
                    continue
            else:
                output += string[i]
                i += 1
                continue
        return output

