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

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """

    def rail_fence_cipher(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """

    def caesar_cipher_with_iv(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher, with the IV.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher_with_iv("abc", 1)
        'bcd'

        """

    def vigenere_cipher_with_iv(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher, with the IV.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher_with_iv("abc")
        'kfa'

        """

    def rail_fence_cipher_with_iv(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher, with the IV.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails to encrypt, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher_with_iv("abc", 2)
        'acb'

        """

    def caesar_cipher_with_iv_and_key(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher, with the IV and the key.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher_with_iv_and_key("abc", 1)
        'bcd'

        """

    def vigenere_cipher_with_iv_and_key(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher, with the IV and the key.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher_with_iv_and_key("abc")
        'kfa'

        """

    def rail_fence_cipher_with_iv_and_key(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher, with the IV and the key.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rails to encrypt, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher_with_iv_and_key("abc", 2)
        'acb'

        """

    def caesar_cipher_with_iv_and_key_and_iv(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher, with the IV and the key.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher_with_iv_and_key_and_iv("abc", 1)
        'bcd'

        """

    def vigenere_cipher_with_iv_and_key_and_iv(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher, with the IV and the key.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher_with_iv_and_key_and_iv("abc")
        'kfa'

        """

    def rail_fence_cipher_with_iv_and_key_and_iv(self,plain_text, rails):
        """
        Encrypts the plaintext