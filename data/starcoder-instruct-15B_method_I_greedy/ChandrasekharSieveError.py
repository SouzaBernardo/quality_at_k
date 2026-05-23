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
        primes = [True] * (self.n + 1)
        primes[0], primes[1] = False, False

        n = 2
        while n * n <= self.n:
            if primes[n]:
                for i in range(n * n, self.n + 1, n):
                    primes[i] = False
            n += 1

        return [i for i in range(2, self.n + 1) if primes[i]]

    def get_primes(n):
        """
        Get the list of primes up to the specified limit.
        :param n: int, the upper limit for generating primes
        :return: list, a list of primes
        >>> get_primes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    
        """
        cs = ChandrasekharSieve(n)
        return cs.get_primes()