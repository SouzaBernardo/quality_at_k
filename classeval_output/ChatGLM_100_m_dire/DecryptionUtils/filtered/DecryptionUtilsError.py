class DecryptionUtils: 
    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key





    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
    
        """
        # Convert the ciphertext to binary
        ciphertext_bin = bytearray(ciphertext)
        
        # Calculate the Vigenere shift
        shift = ((ciphertext_bin[0] << 8) | (ciphertext_bin[1] << 6) | (ciphertext_bin[2] << 4) | (ciphertext_bin[3] << 2) | (ciphertext_bin[4] << 0))
        
        # Calculate the Vigenere key
        key = ((ciphertext_bin[5] << 16) | (ciphertext_bin[6] << 11) | (ciphertext_bin[7] << 7) | (ciphertext_bin[8] << 4) | (ciphertext_bin[9] << 2) | (ciphertext_bin[10] << 0))
        
        # Decipher the Vigenere cipher
        plaintext =''.join([str(x) for x in range(11, 0, -1) if x % 2 == 0])
        
        return plaintext

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        """
        return''.join([f'\x{c}' if c.isalnum() else f'\u{c}' for c in encrypted_text])