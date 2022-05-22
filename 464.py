from functools import lru_cache
from typing import Tuple


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(integer: Tuple, round: int, curSum: int):
            for i in range(len(integer)):
                leftInteger = (*integer[:i], *integer[i+1:])
                nextSum = curSum + integer[i]
                if nextSum >= desiredTotal:
                    return round & 1 == 0
                if round & 1 == 0:
                    if dfs(leftInteger, round+1, nextSum):
                        return True
                else:
                    if not dfs(leftInteger, round+1, nextSum):
                        return False
                
            return round & 1 == 1

        integer = tuple(range(1, maxChoosableInteger+1))
        return sum(integer) >= desiredTotal and dfs(integer, 0, 0)


# print(Solution().canIWin(10, 11))
# print(Solution().canIWin(10, 0))
# print(Solution().canIWin(10, 1))
print(Solution().canIWin(4, 6))