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
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        ciphertext = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    shift = ord(self.key[key_index % len(self.key)].upper()) - 65
                    ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
                    key_index += 1
                else:
                    shift = ord(self.key[key_index % len(self.key)].lower()) - 97
                    ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
                    key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        if rails <= 1:
            return plaintext
        fence = [""] * rails
        direction = 1
        for char in plaintext:
            fence[0] += char
            for i in range(rails - 1):
                if direction == 1:
                    if i == rails - 2:
                        direction = -1
                    if fence[i + 1] == "":
                        fence[i + 1] = char
                    else:
                        fence[i + 1] += char
                else:
                    if i == 0:
                        direction = 1
                    if fence[i - 1] == "":
                        fence[i - 1] = char
                    else:
                        fence[i - 1] += char
        return "".join(fence)