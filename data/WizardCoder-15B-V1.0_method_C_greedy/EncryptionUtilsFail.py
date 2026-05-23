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
                shift = ord(self.key[key_index % len(self.key)].upper()) - 65
                if char.isupper():
                    ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        # Create a matrix with the plain text and empty strings for the ciphertext
        matrix = [[''] * len(plain_text) for _ in range(rails)]
        # Fill the matrix with the plain text
        row, direction = 0, 1
        for char in plain_text:
            matrix[row][row] = char
            row += direction
            if row == 0 or row == rails - 1:
                direction *= -1
        # Create the ciphertext by reading the matrix row by row
        ciphertext = ''
        for row in matrix:
            ciphertext += ''.join(row)
        return ciphertext