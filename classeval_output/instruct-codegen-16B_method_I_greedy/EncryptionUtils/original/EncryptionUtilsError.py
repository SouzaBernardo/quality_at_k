
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
                char_index = ord(char) - ord('a')
                char_shifted = (char_index + shift) % 26
                char_encrypted = chr(char_shifted + ord('a'))
                ciphertext += char_encrypted
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(plaintext, key):
        ciphertext = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                key_char = key[key_index]
                key_index = (key_index + 1) % len(key)
                char_index = ord(char) - ord('a')
                char_shifted = (char_index + ord(key_char)) % 26
                char_encrypted = chr(char_shifted + ord('a'))
                ciphertext += char_encrypted
            else:
                ciphertext += char
        return ciphertext

    def rail_fence_cipher(plain_text, rails):
        # Create an empty ciphertext string
        cipher_text = ""
        # Loop through each character in the plaintext
        for i in range(len(plain_text)):
            # Add the character to the ciphertext if it is not a space
            if plain_text[i]!='':
                # Move to the next rail if we have reached the end
                if i % rails == 0:
                    cipher_text +=''
                else:
                    cipher_text += plain_text[i]
        # Return the ciphertext
        return cipher_text