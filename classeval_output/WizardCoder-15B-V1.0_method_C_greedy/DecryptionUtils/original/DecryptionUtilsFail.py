
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
                if char.isupper():
                    plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
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
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].upper()) - 65
                if char.isupper():
                    plaintext += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - shift - 97) % 26 + 97)
                key_index += 1
            else:
                plaintext += char
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        # Determine the length of each fence and the number of characters in each fence
        fence_length = len(encrypted_text) // rails
        fence_chars = [""] * rails
    
        # Create a list of fences
        fences = [fence_chars.copy() for _ in range(rails)]
    
        # Iterate through the ciphertext, adding each character to the appropriate fence
        index = 0
        for i in range(rails):
            for j in range(fence_length):
                if index < len(encrypted_text):
                    fences[i][j] = encrypted_text[index]
                    index += 1
    
        # Join the characters in each fence to form the deciphered plaintext
        deciphered_text = ""
        for i in range(fence_length):
            for j in range(rails):
                if fences[j][i]!= "":
                    deciphered_text += fences[j][i]
    
        return deciphered_text
    