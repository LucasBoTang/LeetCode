class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eeatosthese
        if n <= 2:
            return 0
        primes = [True] * n
        primes[:2] = [False, False]
        for prime in range(2, int(n ** 0.5) + 1):
            if primes[prime]:
                primes[prime * prime:n:prime] = [False] * len(primes[prime * prime:n:prime])
        return sum(primes)
