
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
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'

        """
        pass


    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext))

    def vigenere_cipher(self, plaintext, rails=None):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rail to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", rails=e.rail_fence_cipher("abc"))
        'kfa'
        >>> e.vigenere_cipher("abc", rails=e.rail_fence_cipher("abc"))
        'kfa'
        """
        if rails is None:
            rails = self.rail_fence_cipher(plaintext)
        return self.vigenere_cipher(plaintext, rails)

    def vigenere_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rail to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", rails=e.rail_fence_cipher("abc"))
        'kfa'
        >>> e.vigenere_cipher("abc", rails=e.rail_fence_cipher("abc"))
        'kfa'
        """
        if rails is None:
            rails = self.rail_fence_cipher(plaintext)
        return self.vigenere_cipher(plaintext, rails)


    def rail_fence_cipher(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        pass


