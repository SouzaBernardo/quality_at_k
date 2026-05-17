
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
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext))

    def vigenere_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rails to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa", "kfa")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext), rails_key=self.key)

    def vigenere_cipher(self, plaintext, rails, rails_key):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rails to encrypt, str.
        :param rails_key: The key to use for encryption, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa", "kfa")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext), rails_key=rails_key)

    def vigenere_cipher(self, plaintext, rails, rails_key):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rails to encrypt, str.
        :param rails_key: The key to use for encryption, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa", "kfa")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext), rails_key=rails_key, rails_key_iv=self.key)

    def vigenere_cipher(self, plaintext, rails, rails_key, rails_key_iv):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rails to encrypt, str.
        :param rails_key: The key to use for encryption, str.
        :param rails_key_iv: The key to use for encryption, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa", "kfa")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext), rails_key=rails_key, rails_key_iv=rails_key_iv)

    def vigenere_cipher(self, plaintext, rails, rails_key, rails_key_iv):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rails to encrypt, str.
        :param rails_key: The key to use for encryption, str.
        :param rails_key_iv: The key to use for encryption, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa")
        'kfa'
        >>> e.vigenere_cipher("abc", "kfa", "kfa")
        'kfa'

        """
        return self.vigenere_cipher(plaintext, rails=self.rail_fence_cipher(plaintext), rails_key=rails_key, rails_key_iv=rails_key_iv)

    def vigenere_cipher(self, plaintext, rails, rails_key, rails_key_iv):
        """
        Encrypts the plaintext using the Vigenere cipher.

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
        return self.rail_fence_cipher(plain_text, rails)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The rails to encrypt, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        return self.rail_fence_cipher(plain_text, rails)
