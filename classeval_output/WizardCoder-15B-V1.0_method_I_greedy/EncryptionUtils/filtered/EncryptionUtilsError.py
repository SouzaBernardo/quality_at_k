class EncryptionUtils:  
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

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
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    shift = ord(self.key[key_index].upper()) - 65
                else:
                    shift = ord(self.key[key_index].lower()) - 97
                if char.isupper():
                    ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
                key_index = (key_index + 1) % len(self.key)
            else:
                ciphertext += char
        return ciphertext