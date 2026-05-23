class EncryptionUtils: 
    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key



    def caesar_cipher(plaintext, shift):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_value = ord(char)
                ascii_value += shift
                if ascii_value > ord('z'):
                    ascii_value -= 26
                elif ascii_value < ord('a'):
                    ascii_value += 26
                
                ciphertext += chr(ascii_value)
            else:
                ciphertext += char
        return ciphertext

    def vigenere_cipher(plaintext, key):
        ciphertext = ""
        key_index = 0
        for character in plaintext:
            if character == " ":
                ciphertext += " "
                continue
            shift = ord(key[key_index]) % 26
            key_index += 1
            if key_index == len(key):
                key_index = 0
                
            shifted_char_code = ord(character) + shift
            if shifted_char_code > ord('z'):
                shifted_char_code -= 26
            ciphertext += chr(shifted_char_code)
        return ciphertext

    def rail_fence_cipher(plain_text, rails):
        # Create an empty list to store the ciphertext
        cipher_text = []
        # Loop through the plaintext and encrypt each character
        for i in range(rails):
            # Create a list to store the characters on each row
            row = []
            # Loop through the plaintext
            for char in plain_text:
                # Add the character to the row
                row.append(char)
                # Join the row list to form the ciphertext
                cipher_text.append(''.join(row))
                # Move to the next row
                row = []
            # Join the list of rows to form the ciphertext
            cipher_text = ''.join(cipher_text)
        return cipher_text