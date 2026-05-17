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

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """

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

    def decrypt_string(self, ciphertext, key):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the decrypted plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_string('ifmmp', 'key')
        'hello'

        """

    def decrypt_string_with_key(self, ciphertext, key):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the decrypted plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_string_with_key('ifmmp', 'key')
        'hello'

        """

    def decrypt_string_with_key_and_iv(self, ciphertext, key, iv):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the decrypted plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_string_with_key_and_iv('ifmmp', 'key', 'iv')
        'hello'

        """

    def decrypt_string_with_key_and_iv_and_cipher(self, ciphertext, key, iv, cipher):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the decrypted plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :param cipher: The cipher to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_string_with_key_and_iv_and_cipher('ifmmp', 'key', 'iv', 'cipher')
        'hello'

        """

    def decrypt_string_with_key_and_iv_and_cipher_and_iv(self, ciphertext, key, iv, cipher, iv_str):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the decrypted plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :param cipher: The cipher to use for decryption,str.
        :param iv_str: The initialization vector to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_string_with_key_and_iv_and_cipher_and_iv('ifmmp', 'key', 'iv', 'cipher', 'iv_str')
        'hello'

        """

    def decrypt_string_with_key_and_iv_and_cipher_and_iv_and_cipher(self, ciphertext, key, iv, cipher, iv_str, cipher_str):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the decrypted plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :param cipher: The cipher to use for decryption,str.
        :param iv_str: The initialization vector to use for decryption,str.
        :param cipher_str: The cipher to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_string_with_key_and_iv_and_cipher_and_iv_and_cipher('ifmmp', 'key', 'iv', 'cipher', 'iv_str', 'cipher_str')
        'hello'

        """

    def decrypt_string