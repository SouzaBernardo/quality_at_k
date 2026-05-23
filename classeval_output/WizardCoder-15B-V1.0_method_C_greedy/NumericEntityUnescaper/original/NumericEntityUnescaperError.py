
class NumericEntityUnescaper: 
    def __init__(self):
        pass



    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        """
        result = ""
        i = 0
        while i < len(string):
            if string[i] == '&':
                if i + 2 < len(string) and string[i+1] == '#' and string[i+2] == 'x':
                    # hexadecimal entity
                    j = i + 3
                    while j < len(string) and self.is_hex_char(string[j]):
                        j += 1
                    if j < len(string) and string[j] == ';':
                        try:
                            char_code = int(string[i+3:j], 16)
                            result += chr(char_code)
                            i = j + 1
                        except ValueError:
                            result += '&' + string[i:j+1]
                            i = j + 1
                    else:
                        result += '&' + string[i:j+1]
                        i = j + 1
                else:
                    # decimal entity
                    j = i + 1
                    while j < len(string) and string[j].isdigit():
                        j += 1
                    if j < len(string) and string[j] == ';':
                        try:
                            char_code = int(string[i+1:j])
                            result += chr(char_code)
                            i = j + 1
                        except ValueError:
                            result += '&' + string[i:j+1]
                            i = j + 1
                    else:
                        result += '&' + string[i:j+1]
                        i = j + 1
            else:
                result += string[i]
                i += 1
        return result

