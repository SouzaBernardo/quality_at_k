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

    def decrypt(self, ciphertext, key):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt('ifmmp', 'key')
        'hello'

        """

    def decrypt_with_key(self, ciphertext, key):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_with_key('ifmmp', 'key')
        'hello'

        """

    def encrypt(self, plaintext, key):
        """
        Encrypts the given plaintext using the Caesar cipher, and returns the ciphertext.
        :param plaintext: The plaintext to encrypt,str.
        :param key: The key to use for encryption,str.
        :return: The encrypted ciphertext,str.
        >>> d = DecryptionUtils('key')
        >>> d.encrypt('ifmmp', 'key')
        'ybocl'

        """

    def encrypt_with_key(self, plaintext, key):
        """
        Encrypts the given plaintext using the Caesar cipher, and returns the ciphertext.
        :param plaintext: The plaintext to encrypt,str.
        :param key: The key to use for encryption,str.
        :return: The encrypted ciphertext,str.
        >>> d = DecryptionUtils('key')
        >>> d.encrypt_with_key('ifmmp', 'key')
        'ybocl'

        """

    def decrypt_with_key_and_iv(self, ciphertext, key, iv):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_with_key_and_iv('ifmmp', 'key', 'iv')
        'hello'

        """

    def decrypt_with_key_and_iv_and_aad(self, ciphertext, key, iv, aad):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :param aad: The additional authentication data to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_with_key_and_iv_and_aad('ifmmp', 'key', 'iv', 'aad')
        'hello'

        """

    def decrypt_with_key_and_iv_and_aad_and_tag(self, ciphertext, key, iv, aad, tag):
        """
        Decrypts the given ciphertext using the Caesar cipher, and returns the plaintext.
        :param ciphertext: The ciphertext to decrypt,str.
        :param key: The key to use for decryption,str.
        :param iv: The initialization vector to use for decryption,str.
        :param aad: The additional authentication data to use for decryption,str.
        :param tag: The tag to use for decryption,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_with_key_and_iv_and_aad_and_tag('ifmmp', 'key', 'iv', 'aad', 'tag')
        'hello'

        """

    def decrypt_with_key_and_iv_and_aad_and_