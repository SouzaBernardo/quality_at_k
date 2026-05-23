class EncryptionUtils: 
    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key





    def vigenere_cipher(plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        """
        key = "key"  # Replace with your own key
        ciphertext = ""
        for i in range(len(plaintext)):
            c = plaintext[i]
            if c == key:
                ciphertext += key[i]
            else:
                ciphertext += ciphertext[i] + key[i]
        return ciphertext