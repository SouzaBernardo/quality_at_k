
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
        """
        # Initialize the list of prime numbers
        primes = []
        # Initialize the number to be tested
        n = 2
        # Keep looping until the limit is reached
        while n < self.n:
            # If the number is prime, add it to the list
            if self.is_prime(n):
                primes.append(n)
            # Increment the number
            n += 1
        return primes


    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes