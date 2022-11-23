from typing import List


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnter = Counter()
        for num in range(lowLimit, highLimit + 1):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            cnter[s] += 1
        return max(cnter.values())
