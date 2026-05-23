```
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
        shift = int(shift)
        new_plaintext = ""
        for i in range(len(plaintext)):
            if shift > 0:
                new_plaintext += plaintext[i]
                shift -= 1
            elif shift < 0:
                new_plaintext += plaintext[i]
                shift += 1
            else:
                new_plaintext += plaintext[i]
        return new_plaintext.encode()

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        plaintext = plaintext.encode()
        key = self.key
        for i in range(len(plaintext)):
            if i % 2 == 1:
                c = plaintext[i]
                for j in range(len(key)):
                    key[j] = key[j] ^ ord(c)
        return key

    def rail_fence_cipher(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        plaintext = plaintext.encode()
        key = self.key
        for i in range(len(plaintext)):
            for j in range(i+1, len(plaintext)):
                for k in range(i, len(plaintext)):
                    key = key + key[1:]
                key = key[len(key) - 1] + plaintext[i]
                key = key + key[1:]
                key = key[len(key) - 1] + plaintext[j]
                key = key + key[1:]
                key = key[len(key) - 1] + plaintext[k]
                key = key + key[1:]
        return key.encode()
```
```