from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [inter[0] for inter in intervals]
        mp = {}
        for i, v in enumerate(starts):
            mp[v] = i
        
        starts.sort()
        n = len(starts)
        ans = [-1] * n
        
        for i in range(n):
            idx = bisect_left(starts, intervals[i][1])
            if idx == n:
                ans[i] = -1
            else:
                ans[i] = mp[starts[idx]]
        return ans