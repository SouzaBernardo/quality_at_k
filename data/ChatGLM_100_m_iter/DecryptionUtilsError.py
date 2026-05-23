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
        # Convert the ciphertext to lowercase
        ciphertext = ciphertext.lower()
        # Calculate the shift
        shift = int(ciphertext.replace('f', 'a').replace('m', 'p').replace('m', 'p').replace(' ', '').replace(' ', '').replace(' ', '').replace('i', 'd').replace('d', 'i').replace('k', 'g').replace('g', 'k'))
        # Decipher the ciphertext using the Caesar cipher
        plaintext =''.join([str(x) for x in ciphertext if x not in ['i', 'd']])
        return plaintext

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
        # Use the Caesar cipher to decipher the ciphertext
        plaintext = d.caesar_decipher(ciphertext)
        # Convert the deciphered plaintext to uppercase
        plaintext = ''.join([str(x) for x in plaintext if x not in ['i', 'd']])
        return plaintext


    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
        # Calculate the number of rails
        rails = int(rails)
        # Calculate the number of spaces to use for decryption
        spaces = int(len(encrypted_text) - len(encrypted_text.replace(' ', '')))
        # Use the rail fence cipher to decipher the ciphertext
        plaintext = ''
        for i in range(rails):
            plaintext +='' * (i + spaces)
        return plaintext