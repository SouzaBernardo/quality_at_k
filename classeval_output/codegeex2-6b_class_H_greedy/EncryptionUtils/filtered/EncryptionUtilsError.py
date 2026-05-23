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
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'

        """
        ciphertext = ""
        for i in range(len(plaintext)):
            ciphertext += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        ciphertext = ""
        key = self.key
        for i in range(len(plaintext)):
            ciphertext += chr((ord(plaintext[i]) + ord(key[i % len(key)]) - 97) % 26 + 97)
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
        ciphertext = ""
        plain_text = list(plain_text)
        for i in range(rails - 1):
            for j in range(i, len(plain_text), rails):
                ciphertext += plain_text[j]
        for i in range(rails - 1):
            for j in range(i, len(plain_text), rails):
                ciphertext += plain_text[j]
        for i in range(len(plain_text)):
            if ciphertext[i] == " ":
                ciphertext = ciphertext[:i] + " " + ciphertext[i + 1 :]
        return ciphertext