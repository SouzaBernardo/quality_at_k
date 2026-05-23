
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
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                deciphered_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                plaintext += deciphered_char
            else:
                plaintext += char
        return plaintext
    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        key = self.key
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext
    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        # Create a matrix to store the zigzag pattern
        matrix = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]
    
        # Define the direction of the zigzag pattern
        direction_down = False
        row, col = 0, 0
    
        # Fill the zigzag pattern
        for i in range(len(encrypted_text)):
            if (row == 0) or (row == rails - 1):
                direction_down = not direction_down
            matrix[row][col] = '*'
            col += 1
            if direction_down:
                row += 1
            else:
                row -= 1
    
        # Fill the ciphertext into the zigzag pattern
        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if matrix[i][j] == '*' and index < len(encrypted_text):
                    matrix[i][j] = encrypted_text[index]
                    index += 1
    
        # Read the plaintext from the zigzag pattern
        result = []
        row, col = 0, 0
        for i in range(len(encrypted_text)):
            if (row == 0) or (row == rails - 1):
                direction_down = not direction_down
            if col < len(encrypted_text):
                result.append(matrix[row][col])
                col += 1
            if direction_down:
                row += 1
            else:
                row -= 1
    
        return ''.join(result)
