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
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = ''
        for i in range(len(plaintext)):
            key_char = self.key[i % len(self.key)]
            plaintext_char = plaintext[i]
            ascii_offset = ord('a') if plaintext_char.islower() else ord('A')
            ciphertext += chr((ord(plaintext_char) + ord(key_char) - 2 * ascii_offset) % 26 + ascii_offset)
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
        rail = 0
        change = 1

        for char in plaintext:
            fence[rail].append(char)
            if rail == 0:
                change = 1
            elif rail == rails - 1:
                change = -1
            rail += change

        ciphertext = ''
        for rail in fence:
            for char in rail:
                if char != '':
                    ciphertext += char
        return ciphertext