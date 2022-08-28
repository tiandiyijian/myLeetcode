from typing import List

from sympy import per


class Solution:
    def fullBloomFlowers1(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        n = len(flowers)
        dp = [0] * (10**9+2)
        for start, end in flowers:
            dp[start] += 1
            dp[end+1] -= 1
        
        for i in range(1, len(dp)):
            dp[i] += dp[i-1]
        
        return [dp[day] for day in persons]

    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # 应该是用线段树, 数据范围太大用差分数组直接爆了
        # 可惜不会
        # 看了答案发现还是用差分数组的思想, 太妙了
        events = []
        for start, end in flowers:
            events.append([start, -1, 1])
            events.append([end+1, -1, -1])
        
        for i, t in enumerate(persons):
            events.append([t, i, 0])
        
        events.sort()

        ans = [0] * (len(persons))
        now = 0
        for t, idx, inc in events:
            now += inc
            if idx >= 0:
                ans[idx] = now

        return ans
        