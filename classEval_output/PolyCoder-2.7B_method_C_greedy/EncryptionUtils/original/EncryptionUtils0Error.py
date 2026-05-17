
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
        return self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self.key + self

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, "vigenere")

    def vigenere_cipher(self, plaintext, cipher_name):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param cipher_name: The name of the cipher to use, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, cipher_name, "vigenere")

    def vigenere_cipher(self, plaintext, cipher_name, cipher_type):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param cipher_name: The name of the cipher to use, str.
        :param cipher_type: The type of cipher to use, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, cipher_name, cipher_type, "vigenere")

    def vigenere_cipher(self, plaintext, cipher_name, cipher_type, cipher_mode):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param cipher_name: The name of the cipher to use, str.
        :param cipher_type: The type of cipher to use, str.
        :param cipher_mode: The mode of cipher to use, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, cipher_name, cipher_type, cipher_mode, "vigenere")

    def vigenere_cipher(self, plaintext, cipher_name, cipher_type, cipher_mode, cipher_name_mode):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param cipher_name: The name of the cipher to use, str.
        :param cipher_type: The type of cipher to use, str.
        :param cipher_mode: The mode of cipher to use, str.
        :param cipher_name_mode: The mode of cipher to use, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, cipher_name, cipher_type, cipher_mode, cipher_name_mode, "vigenere")

    def vigenere_cipher(self, plaintext, cipher_name, cipher_type, cipher_mode, cipher_name_mode, cipher_mode_name):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param cipher_name: The name of the cipher to use, str.
        :param cipher_type: The type of cipher to use, str.
        :param cipher_mode: The mode of cipher to use, str.
        :param cipher_name_mode: The mode of cipher to use, str.
        :param cipher_mode_name: The mode of cipher to use, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, cipher_name, cipher_type, cipher_mode, cipher_name_mode, cipher_mode_name, "vigenere")

    def vigenere_cipher(self, plaintext, cipher_name, cipher_type, cipher_mode, cipher_name_mode, cipher_mode_name, cipher_name_mode_name):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param cipher_name: The name of the cipher to use, str.
        :param cipher_type: The type of cipher to use, str.
        :param cipher_mode: The mode of cipher to use, str.
        :param cipher_name_mode: The mode of cipher to use, str.
        :param cipher_mode_name: The mode of cipher to use, str.
        :param cipher_name_mode_name: The mode of cipher to use, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, cipher_name, cipher_type, cipher_mode, cipher_name_mode, cipher_mode_name, cipher_name_mode_name, "vigenere")


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
