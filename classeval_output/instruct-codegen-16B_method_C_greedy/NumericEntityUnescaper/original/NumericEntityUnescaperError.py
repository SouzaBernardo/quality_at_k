
class NumericEntityUnescaper: 
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
            if string[i] == '&' and (i + 1 < len(string) and string[i + 1] == '#'):
                char_code = ""
                i += 2
                while i < len(string):
                    if string[i] == ';':
                        break
                    char_code += string[i]
                    i += 1
                if char_code.isnumeric():
                    output += chr(int(char_code))
                else:
                    output += '&#' + char_code + ';'
            else:
                output += string[i]
            i += 1
        return output

