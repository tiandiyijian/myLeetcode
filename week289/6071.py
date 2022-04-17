from typing import List
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnter = Counter(tasks)
        ans = 0
        for cnt in cnter.values():
            flag = False
            for q in range(cnt // 3, -1, -1):
                if (left := cnt - 3*q) & 1 == 0:
                    p = left >> 1
                    ans += (p + q)
                    flag = True
                    break
            if not flag:
                return -1
        return ans

print(Solution().minimumRounds([2,2,3,3,2,4,4,4,4,4]))
print(Solution().minimumRounds([2,3,3]))