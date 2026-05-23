
class DecryptionUtils: 
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
            if ord(char) >= ord('a') and ord(char) <= ord('z'):
                plaintext += chr((ord(char) - ord('a') + shift) % 26)
            else:
                plaintext += chr((ord(char) - ord('0') + shift) % 10)
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ""
        for char in ciphertext:
            plaintext += char
            if char == self.key:
                plaintext += self.key
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        # Define the plaintext as an empty string
        plaintext = ""
    
        # Loop through the encrypted_text using the rails
        for i in range(rails):
            # Get the current character in the encrypted_text
            char = encrypted_text[i]
    
            # If the character is a space, add it to the plaintext
            if char == " ":
                plaintext += char
    
            # If the character is not a space, add it to the plaintext
            else:
                # Get the index of the character in the key
                index = self.key.index(char)
    
                # Add the index to the plaintext
                plaintext += str(index)
    
        # Return the deciphered plaintext
        return plaintext