
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
        """
        plaintext = ""
        for char in ciphertext:
            if char == " ":
                continue
            shifted_char = chr((ord(char) - shift))
            plaintext += shifted_char
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        """
        plaintext = ""
        for char in ciphertext:
            if char == " ":
                continue
            plaintext += chr(ord(char) ^ self.key[0])
        plaintext = plaintext.zfill(len(ciphertext))
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
            """
            Deciphers the given ciphertext using the Rail Fence cipher
            :param encrypted_text: The ciphertext to decipher,str.
            :param rails: The number of rails to use for decryption,int.
            :return: The deciphered plaintext,str.
            """
            plaintext = ""
            for i in range(rails):
                for j in range(encrypted_text.count(" ")):
                    if encrypted_text[j:j+2] == "..":
                        plaintext += " "
                    else:
                        plaintext += encrypted_text[j:j+2]
            return plaintext