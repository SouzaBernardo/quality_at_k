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
        Encrypts the plaintext and ciphertext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param ciphertext: The ciphertext to decrypt, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt_and_decrypt("abc", "abc")
        'abc'

        """

    def decrypt_and_encrypt(self, ciphertext, plaintext):
        """
        Decrypts the ciphertext and plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param plaintext: The plaintext to encrypt, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_encrypt("abc", "abc")
        'abc'

        """

    def encrypt_and_decrypt_and_verify(self, plaintext, ciphertext, key):
        """
        Encrypts the plaintext and ciphertext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param ciphertext: The ciphertext to decrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt_and_decrypt_and_verify("abc", "abc", "key")
        'abc'

        """

    def decrypt_and_verify(self, ciphertext, key):
        """
        Decrypts the ciphertext and plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_verify("abc", "key")
        'abc'

        """

    def encrypt_and_decrypt_and_verify(self, plaintext, ciphertext, key):
        """
        Encrypts the plaintext and ciphertext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param ciphertext: The ciphertext to decrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt_and_decrypt_and_verify("abc", "abc", "key")
        'abc'

        """

    def decrypt_and_verify(self, ciphertext, key):
        """
        Decrypts the ciphertext and plaintext using the Caesar cipher.
        :param ciphertext: The ciphertext to decrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.decrypt_and_verify("abc", "key")
        'abc'

        """

    def encrypt_and_decrypt_and_verify(self, plaintext, ciphertext, key):
        """
        Encrypts the plaintext and ciphertext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param ciphertext: The ciphertext to decrypt, str.
        :param key: The key to use for encryption, str.
        :return: The plaintext, str.
        >>> e = EncryptionUtils("key")
        >>> e.encrypt_and_decrypt_and_verify("abc", "abc", "key")
     