
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
        shift_chars = [chr(ord(c) + shift) for c in plaintext]
        return ''.join(shift_chars)

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        key_indices = {}
        for i in range(len(plaintext)):
            key_indices[plaintext[i]] = i
        for i in range(len(plaintext)):
            if plaintext[i] in key_indices:
                key_indices[plaintext[i]] += 1
            else:
                key_indices[plaintext[i]] = 1
        for i in range(len(key_indices)):
            key_indices[key_indices[i]] = i
        for i in range(len(plaintext)):
            cipher_text += plaintext[i] + key_indices[plaintext[i]]
        return cipher_text

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: A list of integers representing the rails of the rail fence cipher.
        :return: The ciphertext, str.
        """
        num_rails = len(rails)
        num_plain_text_chars = len(plain_text)
        for i in range(num_plain_text_chars):
            for j in range(num_rails):
                if plain_text[i] == 'a':
                    plain_text[i] = rails[j]
                elif plain_text[i] == 'b':
                    plain_text[i] = rails[j] + 1
                elif plain_text[i] == 'c':
                    plain_text[i] = rails[j] + 2
                #...
        return plain_text