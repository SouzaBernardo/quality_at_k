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
        # Convert the plaintext to lowercase
        plaintext = plaintext.lower()

        # Shift the characters in the plaintext by the specified number of positions
        ciphertext = ""
        for i in range(len(plaintext)):
            ciphertext += plaintext[i] + shift * len(plaintext[i])

        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        # Convert the plaintext to lowercase
        plaintext = plaintext.lower()

        # Shift the characters in the plaintext by the specified number of positions
        ciphertext = ""
        for i in range(len(plaintext)):
            ciphertext += plaintext[i] + (self.key**i) * len(plaintext[i])

        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rows to encrypt, int.
        :return: The ciphertext, str.
        """
        # Convert the plaintext to lowercase
        plaintext = plaintext.lower()

        # Create a 2D array of characters to encrypt
        ciphertext = []
        for i in range(len(plaintext)):
            row = []
            for j in range( Rails):
                row.append(plaintext[i])
            ciphertext.append(row)

        # Encrypt the rows of the 2D array
        for i in range(len(ciphertext)):
            row = []
            for j in range( Rails):
                row.append(ciphertext[i])
            ciphertext[i] = "".join([str(c) for c in row])

        return ciphertext