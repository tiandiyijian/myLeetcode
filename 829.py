class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        n *= 2
        for k in range(1, int(pow(n, 0.5)) + 1):
            if n % k == 0:
                if (n // k - (k - 1)) % 2 == 0:
                    ans += 1
        return ans
