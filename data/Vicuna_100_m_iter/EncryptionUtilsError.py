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
        # Convert the plaintext to lowercase
        plaintext = plaintext.lower()
    
        # Convert the shift to an integer
        shift = int(shift)
    
        # Iterate through the plaintext
        for i in range(len(plaintext)):
            # Shift the plaintext
            j = (i + shift) % len(plaintext)
    
            # Substitute the shifted plaintext with the ciphertext
            plaintext[i:j] = plaintext[j:i]
    
        # Convert the plaintext back to uppercase
        ciphertext = plaintext.upper()
    
        return ciphertext

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        # Convert the plaintext to lowercase
        plaintext = plaintext.lower()
    
        # Initialize the key with the plaintext
        key = plaintext
    
        # Convert the key to an integer
        key = int(key)
    
        # Iterate through the plaintext
        for i in range(len(plaintext)):
            # Get the first and second halves of the key
            key_half1 = key[:i]
            key_half2 = key[i:]
    
            # XOR the first and second halves of the key with the plaintext
            plaintext[i] = chr(ord(plaintext[i]) ^ ord(key_half1[0]))
    
            # Add the first and second halves of the key to the plaintext
            plaintext[i:i+2] = plaintext[i:i+2] + key_half2
    
        # Convert the plaintext back to uppercase
        ciphertext = plaintext.upper()
    
        return ciphertext

    def rail_fence_cipher(plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plain_text: The plaintext to encrypt, str.
        :param rails: The number of rows to use for the rail fence cipher, int.
        :return: The ciphertext, str.
        """
        # Initialize the key with the plaintext
        key = plain_text
    
        # Convert the key to an integer
        key = int(key)
    
        # Iterate through the plaintext
        for i in range(len(plain_text)):
            # Get the row number of the current character
            row = i // rails
    
            # XOR the current character with the corresponding character in the row
            plain_text[i] = chr(ord(plain_text[i]) ^ ord(key[row]))
    
        # Convert the plaintext back to uppercase
        cipher_text = plain_text.upper()
    
        return cipher_text