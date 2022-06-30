class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        numPrimes = sum(self.isPrime(i) for i in range(1, n + 1))
        return self.factorial(numPrimes) * self.factorial(n - numPrimes) % (10**9 + 7)

    def isPrime(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1

    def factorial(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res *= i
            res %= 10**9 + 7
        return res
