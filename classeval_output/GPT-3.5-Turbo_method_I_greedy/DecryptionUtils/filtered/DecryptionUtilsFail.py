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
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'
        """
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                plaintext += decrypted_char
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
        key_length = len(self.key)
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                key_char = self.key[i % key_length]
                key_shift = ord(key_char) - ascii_offset
                decrypted_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
                plaintext += decrypted_char
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
        # Create a list of empty strings to represent each rail
        rail_strings = [''] * rails
    
        # Initialize variables for tracking the current rail and direction
        current_rail = 0
        direction = 1
    
        # Iterate through each character in the encrypted text
        for char in encrypted_text:
            # Add the character to the current rail
            rail_strings[current_rail] += char
    
            # Update the current rail and direction
            current_rail += direction
    
            # Reverse the direction if we reach the first or last rail
            if current_rail == 0 or current_rail == rails - 1:
                direction *= -1
    
        # Concatenate the rail strings to get the deciphered plaintext
        plaintext = ''.join(rail_strings)
        return plaintext