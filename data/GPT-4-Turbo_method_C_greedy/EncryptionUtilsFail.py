class EncryptionUtils: 
    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key


    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        """
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                cipher_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                ciphertext += cipher_char
            else:
                ciphertext += char
        return ciphertext
    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        key = self.key
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext
    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        cipher = ['' for _ in range(rails)]
        index = 0
        increment = 1
    
        for char in plain_text:
            cipher[index] += char
            if index == 0:
                increment = 1
            elif index == rails - 1:
                increment = -1
            index += increment
    
        return ''.join(cipher)