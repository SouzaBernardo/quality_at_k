Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class NumericEntityUnescaper in the following code.
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
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """


    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """

### Response:The class `NumericEntityUnescaper` is missing the implementation of the `replace` method. Here's the corrected code:

```python
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
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """
        result = ""
        i = 0
        while i < len(string):
            if string[i] == "&":
                if i+2 < len(string) and string[i+1] == "#":
                    if string[i+2] == "x" or string[i+2] == "X":
                        hex_digits = string[i+3:i+9]
                        if len(hex_digits) == 0 or not all(NumericEntityUnescaper.is_hex_char(c) for c in hex_digits):
                            result += "&"
                        else:
                            result += chr(int(hex_digits, 16))
                        i += 8
                    else:
                        digits = string[i+2:i+8]
                        if len(digits) == 0 or not all(c.isdigit() for c in digits):
                            result += "&"
                        else:
                            result += chr(int(digits))
                        i += 7
                else:
                    j = string.find(";", i)
                    if j == -1:
                        result += "&"
                        i += 1
                    else:
                        entity = string[i+1:j]
                        if entity in HTML_ENTITIES:
                            result += HTML_ENTITIES[entity]
                        else:
                            result += "&"
                        i = j
            else:
                result += string[i]
                i += 1
        return result

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
        return char.isdigit() or (char >= 'a' and char <= 'f') or (char >= 'A' and char <= 'F')
```

The `replace` method uses a loop to iterate over each character in the input string. If the character is an ampersand (`&`), it checks whether the next two characters are `#` and then either a `x` or a `X` to indicate that the next characters are hexadecimal digits or decimal digits, respectively. It then extracts the appropriate number of characters and converts them to an integer, and uses that integer to look up the corresponding Unicode character in the `HTML_ENTITIES` dictionary. If the entity is not recognized, it simply adds the ampersand to the result string. Otherwise, it adds the Unicode character to the result string. If the character is not an ampersand, it simply adds it to the result string. Finally, it returns the result string with all numeric character references replaced with their corresponding Unicode characters.

The `is_hex_char` method is a static method that checks whether a given character is a hexadecimal digit. It returns `True` if the character is a digit or a letter between `a` and `f` or between `A` and `F`, respectively.