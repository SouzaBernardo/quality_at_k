class DecryptionUtils:  
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key



    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decipher,str.
        :param shift: The shift to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'
    
        """
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                shift = shift % 26
                if char.islower():
                    plaintext += chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    plaintext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                plaintext += char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
    
        """
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = self.key[key_index].lower() - 97
                if char.islower():
                    plaintext += chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    plaintext += chr((ord(char) - 65 + shift) % 26 + 65)
                key_index = (key_index + 1) % len(self.key)
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
    
        """
        rows = [[''] * len(encrypted_text) for _ in range(rails)]
        dir_down = True
        row = 0
        for char in encrypted_text:
            rows[row][row] = char
            if dir_down:
                row += 1
            else:
                row -= 1
            if row == 0 or row == rails - 1:
                dir_down = not dir_down
        return ''.join([''.join(row) for row in rows])