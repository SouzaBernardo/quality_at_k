def generate_primes(self):
    """
    Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
    :return: list, a list of prime numbers
    """
    primes = []
    sieve = [True] * (self.n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(self.n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, self.n + 1, i):
                sieve[j] = False

    for i in range(2, self.n + 1):
        if sieve[i]:
            primes.append(i)

    return primes