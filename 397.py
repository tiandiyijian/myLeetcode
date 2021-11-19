from functools import lru_cache

class Solution:
    @lru_cache()
    def integerReplacement(self, n: int) -> int:
        if n & (n - 1) == 0:
            return int(log(n, 2))
        if n & 1 == 0:
            return 1 + self.integerReplacement(n >> 1)
        else:
            return 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))