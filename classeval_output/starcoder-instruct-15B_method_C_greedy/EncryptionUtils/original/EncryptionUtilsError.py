
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
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'

        """
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                shift %= 26
                if char.islower():
                    encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += char
        return encrypted_text

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
    
        """
        key = self.key
        ciphertext = ''
        for i, char in enumerate(plaintext):
            shift = key[i % len(key)]
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        return ciphertext

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
    
        """
        fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        dir_down = True
        row, col = 0, 0
    
        for char in plain_text:
            fence[row][col] = char
            if dir_down:
                row += 1
            else:
                col += 1
    
            if row == 0 or row == rails - 1:
                dir_down = not dir_down
    
        return ''.join([''.join(row) for row in fence])