class ChandrasekharSieve:
    """
    This is a class that uses the Chandrasekhar's Sieve method to find all prime numbers within the range
    """

    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        :param n: int, the upper limit for generating prime numbers
        """
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        """
        Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]

        """

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.get_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]

        """

    def is_prime(self, n):
        """
        Check if the given number is prime.
        :param n: int, the number to check
        :return: bool, True if the number is prime, False otherwise
        >>> cs = ChandrasekharSieve(20)
        >>> cs.is_prime(1)
        False
        >>> cs.is_prime(2)
        True
        >>> cs.is_prime(3)
        True
        >>> cs.is_prime(4)
        False
        >>> cs.is_prime(5)
        True
        >>> cs.is_prime(6)
        False
        >>> cs.is_prime(7)
        False
        >>> cs.is_prime(8)
        False
        >>> cs.is_prime(9)
        False
        >>> cs.is_prime(10)
        True
        >>> cs.is_prime(11)
        True
        >>> cs.is_prime(12)
        False
        >>> cs.is_prime(13)
        False
        >>> cs.is_prime(14)
        False
        >>> cs.is_prime(15)
        False
        >>> cs.is_prime(16)
        False
        >>> cs.is_prime(17)
        False
        >>> cs.is_prime(18)
        False
        >>> cs.is_prime(19)
        True
        >>> cs.is_prime(20)
        True

        """

    def is_prime_list(self, n):
        """
        Check if the given list of numbers is prime.
        :param n: list, the list of numbers to check
        :return: bool, True if the list of numbers is prime, False otherwise
        >>> cs = ChandrasekharSieve(20)
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19])
        True
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31])
        True
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53])
        False
        >>> cs.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37