
class DecryptionUtils: 
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
                shift %= 26
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
        key_length = len(self.key)
        plaintext = ''
        for i, char in enumerate(ciphertext):
            shift = i % key_length
            plaintext += chr((ord(char) - 97 + shift) % 26 + 97)
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
        rows = [''] * rails
        column = 0
        for char in encrypted_text:
            rows[column] += char
            column += 1
            if column == rails:
                column = 0
        return ''.join(rows)