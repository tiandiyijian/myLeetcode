from functools import reduce
from operator import or_


class Solution:

    def countPrimeSetBits1(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        ans = 0
        for i in range(left, right + 1):
            cnt = 0
            while i > 0:
                i = i & (i - 1)
                cnt += 1
            ans += 1 if cnt in primes else 0

        return ans
    
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # primes = [2, 3, 5, 7, 11, 13, 17, 19]
        # mask = reduce(or_, (1 << p for p in primes))
        mask = 665772
        # print(mask)
        ans = 0
        for i in range(left, right + 1):
            cnt = 0
            while i > 0:
                i = i & (i - 1)
                cnt += 1
            ans += 1 if (1 << cnt) & mask > 0 else 0

        return ans

print(Solution().countPrimeSetBits(6, 10))