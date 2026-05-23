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
                ascii_offset = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                ciphertext += shifted_char
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
        key_length = len(self.key)
        for i in range(len(plaintext)):
            char = plaintext[i]
            key_char = self.key[i % key_length]
            if char.isalpha():
                char_code = ord(char.upper()) - 65
                key_code = ord(key_char.upper()) - 65
                encrypted_code = (char_code + key_code) % 26
                encrypted_char = chr(encrypted_code + 65)
                ciphertext += encrypted_char
            else:
                ciphertext += char
        return ciphertext
    

    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        fence = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
        rail = 0
        direction = 1
    
        for char in plaintext:
            fence[rail][col] = char
            rail += direction
    
            if rail == 0 or rail == rails - 1:
                direction = -direction
    
        ciphertext = ''
        for rail in fence:
            for char in rail:
                if char != '\n':
                    ciphertext += char
    
        return ciphertext