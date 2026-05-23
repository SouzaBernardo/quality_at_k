class DecryptionUtils: 
    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key



    def caesar_decipher(self, ciphertext, shift):
        plaintext = ""
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if (char.isupper()):
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ''
        i = 0
        for char in ciphertext:
            if (i+1)%len(self.key) == 0:
                i = 0
            plaintext += chr(ord(char) - ord(self.key[i]) + 65)
            i += 1
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        # Create an empty plaintext string
        plaintext = ''
        # Loop over each character in the ciphertext
        for i in range(len(encrypted_text)):
            # Append character to plaintext
            plaintext += encrypted_text[i]
            # If we have reached the end of the rail
            if (i % rails == 0):
                # Reverse the order of characters
                plaintext = self.reverse_string(plaintext)
                # Append the reversed character
                plaintext += encrypted_text[i]
                # Reset the reversed character
                plaintext = self.reverse_string(plaintext)
        # Return the decrypted plaintext
        return plaintext