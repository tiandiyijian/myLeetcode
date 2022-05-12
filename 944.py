from itertools import pairwise
from typing import List

class Solution:
    def minDeletionSize1(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            for i in range(1, len(col)):
                if col[i] < col[i-1]:
                    ans += 1
                    break

        return ans
    
    def minDeletionSize2(self, strs: List[str]) -> int:
        # 第一次见到pairwise这个迭代工具
        return sum(any(x > y for x, y in pairs) for pairs in (pairwise(col) for col in zip(*strs)))
    
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))


strs = ["cba","daf","ghi"]
print(Solution().minDeletionSize(strs))