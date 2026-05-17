
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
        plaintext = ''
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
        plaintext = ''
        key_length = len(self.key)
        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                ascii_offset = ord('a') if ciphertext[i].islower() else ord('A')
                key_char = self.key[i % key_length].lower()
                key_shift = ord(key_char) - ord('a')
                deciphered_char = chr((ord(ciphertext[i]) - ascii_offset - key_shift) % 26 + ascii_offset)
                plaintext += deciphered_char
            else:
                plaintext += ciphertext[i]
        return plaintext
    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        length = len(encrypted_text)
        fence = [['\n' for i in range(length)] for j in range(rails)]
        dir_down = None
        row, col = 0, 0
    
        for i in range(length):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
    
            fence[row][col] = encrypted_text[i]
            col += 1
    
            if dir_down:
                row += 1
            else:
                row -= 1
    
        result = []
        for i in range(rails):
            for j in range(length):
                if fence[i][j] != '\n':
                    result.append(fence[i][j])
        return("".join(result))
