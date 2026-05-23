
class ChandrasekharSieve: 
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
        """
        sieve = [True] * (self.n + 1)
        sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers
        for current in range(2, int(self.n**0.5) + 1):
            if sieve[current]:
                sieve[current**2: self.n + 1: current] = [False] * len(sieve[current**2: self.n + 1: current])
        return [num for num in range(2, self.n + 1) if sieve[num]]

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes

