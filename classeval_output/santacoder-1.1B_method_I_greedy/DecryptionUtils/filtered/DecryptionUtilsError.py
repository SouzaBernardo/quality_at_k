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
        # Create a list of the characters in the ciphertext
        ciphertext_list = list(ciphertext)
        # Create a list of the characters in the key
        key_list = list(self.key)
        # Create a list of the characters in the ciphertext shifted by the shift
        shifted_ciphertext_list = []
        for char in ciphertext_list:
            shifted_ciphertext_list.append(key_list[shift % len(key_list) + ord(char) - ord('a')])
        # Join the list of characters into a string
        deciphered_plaintext = ''.join(shifted_ciphertext_list)
        return deciphered_plaintext


    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
        # Create a list of the characters in the ciphertext
        ciphertext_list = list(ciphertext)
        # Create a list of the characters in the key
        key_list = list(self.key)
        # Create a list of the characters in the ciphertext shifted by the shift
        shifted_ciphertext_list = []
        for char in ciphertext_list:
            shifted_ciphertext_list.append(key_list[ord(char) - ord('a')])
        # Join the list of characters into a string
        deciphered_plaintext = ''.join(shifted_ciphertext_list)
        return deciphered_plaintext



    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
        # Create a list of the characters in the ciphertext
        ciphertext_list = list(encrypted_text)
        # Create a list of the characters in the key
        key_list = list(self.key)
        # Create a list of the characters in the ciphertext shifted by the shift
        shifted_ciphertext_list = []
        for char in ciphertext_list:
            shifted_ciphertext_list.append(key_list[rails % len(key_list) + ord(char) - ord('a')])
        # Join the list of characters into a string
        deciphered_plaintext = ''.join(shifted_ciphertext_list)
        return deciphered_plaintext