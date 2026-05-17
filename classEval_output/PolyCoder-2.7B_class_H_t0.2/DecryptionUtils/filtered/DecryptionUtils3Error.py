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

    def decrypt(self, ciphertext, shift):
        """
        Decrypts the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :param shift: The shift to use for decryption,int.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt('ifmmp', 1)
        'hello'

        """

    def decrypt_vigenere(self, ciphertext):
        """
        Decrypts the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_vigenere('ifmmp')
        'ybocl'

        """

    def decrypt_rail_fence(self, ciphertext, rails):
        """
        Decrypts the given ciphertext using the Rail Fence cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_rail_fence('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """

    def decrypt_decipher(self, ciphertext, shift):
        """
        Decrypts the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :param shift: The shift to use for decryption,int.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_decipher('ifmmp', 1)
        'hello'

        """

    def decrypt_decipher_vigenere(self, ciphertext):
        """
        Decrypts the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_decipher_vigenere('ifmmp')
        'ybocl'

        """

    def decrypt_decipher_rail_fence(self, ciphertext, rails):
        """
        Decrypts the given ciphertext using the Rail Fence cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_decipher_rail_fence('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """

    def decrypt_decipher_decipher(self, ciphertext, shift):
        """
        Decrypts the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :param shift: The shift to use for decryption,int.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_decipher_decipher('ifmmp', 1)
        'hello'

        """

    def decrypt_decipher_decipher_vigenere(self, ciphertext):
        """
        Decrypts the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :return: The decrypted plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.decrypt_decipher_decipher_vigenere('ifmmp')
        'ybocl'

        """

    def decrypt_decipher_decipher_rail_fence(self, ciphertext, rails):
        """
        Decrypts the given ciphertext using the Rail Fence cipher
        :param ciphertext: The ciphertext to decrypt,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The decrypted plaintext,str.
        >>> d