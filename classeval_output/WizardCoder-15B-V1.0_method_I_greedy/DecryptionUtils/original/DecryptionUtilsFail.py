
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
        """
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
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
                if char.isupper():
                    shift = ord(self.key[key_index % len(self.key)].upper()) - 65
                else:
                    shift = ord(self.key[key_index % len(self.key)].lower()) - 97
                if char.isupper():
                    plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
                key_index += 1
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        # Create a matrix to store the decrypted text
        decrypted_matrix = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]
        # Determine the direction of each rail
        direction = 1
        # Fill in the matrix with the decrypted text
        for i in range(len(encrypted_text)):
            current_rail = (i % rails)
            decrypted_matrix[current_rail][i] = encrypted_text[i]
            if current_rail == 0:
                direction = 1
            elif current_rail == rails - 1:
                direction = -1
            else:
                direction = direction
        # Combine the decrypted text from each rail into a single string
        decrypted_text = ''
        for rail in decrypted_matrix:
            decrypted_text += ''.join(rail)
        return decrypted_text