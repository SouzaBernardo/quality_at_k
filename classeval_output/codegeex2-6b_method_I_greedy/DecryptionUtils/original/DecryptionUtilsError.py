
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
        
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    plaintext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                plaintext += char
        return plaintext



    def vigenere_decipher(self, ciphertext, keyword):


    def vigenere_decipher(self, ciphertext):
        

        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    plaintext += chr((ord(char) - ord('A') + ord(self.key[key_index]) - ord('A')) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(char) - ord('a') + ord(self.key[key_index]) - ord('a')) % 26 + ord('a'))
                key_index += 1
                if key_index == len(self.key):
                    key_index = 0
            else:
                plaintext += char
        return plaintext



    def rail_fence_decipher(self, ciphertext, num_rails):


    def rail_fence_decipher(self, encrypted_text, rails):
        
        plaintext = ''
        rail_index = 0
        rails_array = ['' for i in range(rails)]
        for char in encrypted_text:
            if char.isalpha():
                if char.isupper():
                    rails_array[rail_index] += chr((ord(char) - ord('A') + ord(self.key[rail_index]) - ord('A')) % 26 + ord('A'))
                else:
                    rails_array[rail_index] += chr((ord(char) - ord('a') + ord(self.key[rail_index]) - ord('a')) % 26 + ord('a'))
                rail_index += 1
                if rail_index == rails:
                    rail_index = 0
            else:
                rails_array[rail_index] += char
        for rail in rails_array:
            plaintext += rail
        return plaintext
