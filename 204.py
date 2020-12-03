class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        primes = [0] * n
        k = 0
        for i in range(2, n):
            if isPrime[i]:
                primes[k] = i
                k += 1
            for p in primes:
                if i * p >= n:
                    break
                isPrime[i * p] = False
                if i % p == 0:
                    break
        return k


if __name__ == "__main__":
    s = Solution()
    print()