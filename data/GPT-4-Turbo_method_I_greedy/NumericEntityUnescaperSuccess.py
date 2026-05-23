class NumericEntityUnescaper: 
    def __init__(self):
        pass


    def replace(self, string):
        import re
        def decode_entity(m):
            try:
                return chr(int(m.group(1)))
            except ValueError:
                return m.group(0)
    
        return re.sub(r'&#(\d+);', decode_entity, string)
    def is_hex_char(char):
        hex_digits = set("0123456789abcdefABCDEF")
        return char in hex_digits