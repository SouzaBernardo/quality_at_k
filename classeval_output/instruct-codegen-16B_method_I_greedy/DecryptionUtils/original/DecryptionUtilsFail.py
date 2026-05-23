
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
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                char_index = ord(char) - ord('a')
                char_shifted = (char_index - shift) % 26
                if char.isupper():
                    plaintext += chr(ord('A') + (char_shifted % 26))
                else:
                    plaintext += chr(ord('a') + (char_shifted % 26))
            else:
                plaintext += char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                char_index = ord(char) - ord('a')
                char_shifted = (char_index + self.key[key_index]) % 26
                if char.isupper():
                    plaintext += chr(ord('A') + (char_shifted % 26))
                else:
                    plaintext += chr(ord('a') + (char_shifted % 26))
                key_index += 1
                if key_index == len(self.key):
                    key_index = 0
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        plaintext = ""
        row = 0
        for char in encrypted_text:
            if row == 0 or row == rails - 1:
                plaintext += char
                if row == rails - 1:
                    row = 0
                else:
                    row += 1
            else:
                plaintext += char
                row += 1
        return plaintext