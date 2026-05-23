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

    def encrypt(self, plaintext):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt("abc")
        'abc'

        """

    def decrypt(self, ciphertext):
        """
        Decrypts the ciphertext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt("abc")
        'abc'

        """

    def encrypt_and_decrypt(self, plaintext, ciphertext):
        """
        Encrypts the plaintext using the Caesar cipher and decrypts the ciphertext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param ciphertext: The ciphertext to decrypt, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt_and_decrypt("abc", "abc")
        'abc'

        """

    def encrypt_and_decrypt_with_key(self, plaintext, ciphertext, key):
        """
        Encrypts the plaintext using the Caesar cipher and decrypts the ciphertext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param ciphertext: The ciphertext to decrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt_and_decrypt_with_key("abc", "abc", "key")
        'abc'

        """

    def decrypt_and_encrypt(self, ciphertext, plaintext):
        """
        Decrypts the ciphertext using the Caesar cipher and encrypts the plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param plaintext: The plaintext to encrypt, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_encrypt("abc", "abc")
        'abc'

        """

    def decrypt_and_encrypt_with_key(self, ciphertext, plaintext, key):
        """
        Decrypts the ciphertext using the Caesar cipher and encrypts the plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param plaintext: The plaintext to encrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_encrypt_with_key("abc", "abc", "key")
        'abc'

        """

    def decrypt_and_encrypt_with_key_and_iv(self, ciphertext, plaintext, key, iv):
        """
        Decrypts the ciphertext using the Caesar cipher and encrypts the plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param plaintext: The plaintext to encrypt, str.
        :param key: The key to use for encryption, str.
        :param iv: The initialization vector to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_encrypt_with_key_and_iv("abc", "abc", "key", "iv")
        'abc'

        """

    def decrypt_and_encrypt_with_iv(self, ciphertext, plaintext, iv):
        """
        Decrypts the ciphertext using the Caesar cipher and encrypts the plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param plaintext: The plaintext to encrypt, str.
        :param iv: The initialization vector to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_encrypt_with_iv("abc", "abc", "iv")
        'abc'

        """

    def decrypt_and_encrypt_with_iv_and_key(self, ciphertext, plaintext,