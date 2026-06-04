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
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                plaintext += decrypted_char
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
        plaintext = ""
        key_length = len(self.key)
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                key_char = self.key[i % key_length]
                key_shift = ord(key_char) - ascii_offset
                decrypted_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
                plaintext += decrypted_char
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
        """
        fence = [['\n' for _ in range(len(encrypted_text))] for _ in range(rails)]
        rail = 0
        direction = 1
        for char in encrypted_text:
            fence[rail][col] = char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction = -direction
            col += 1
        plaintext = ""
        rail = 0
        for col in range(len(encrypted_text)):
            if fence[rail][col] != '\n':
                plaintext += fence[rail][col]
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction = -direction
        return plaintext