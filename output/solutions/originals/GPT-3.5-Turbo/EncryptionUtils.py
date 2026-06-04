Please complete the class EncryptionUtils in the following code.

```python
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
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
        ciphertext = ""
        key_length = len(self.key)
        for i, char in enumerate(plaintext):
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                key_char = self.key[i % key_length]
                shift = ord(key_char) - ord('a')
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        fence = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
        direction = -1
        row, col = 0, 0
        for char in plaintext:
            if row == 0 or row == rails - 1:
                direction *= -1
            fence[row][col] = char
            col += 1
            row += direction
        ciphertext = ""
        for i in range(rails):
            for j in range(len(plaintext)):
                if fence[i][j] != '\n':
                    ciphertext += fence[i][j]
        return ciphertext
```

This code completes the class EncryptionUtils by implementing the caesar_cipher, vigenere_cipher, and rail_fence_cipher methods. The caesar_cipher method encrypts the plaintext using the Caesar cipher by shifting each character by the specified shift value. The vigenere_cipher method encrypts the plaintext using the Vigenere cipher by shifting each character based on the corresponding character in the key. The rail_fence_cipher method encrypts the plaintext using the Rail Fence cipher by arranging the characters in a zigzag pattern.