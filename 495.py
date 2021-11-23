from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        n = len(timeSeries)
        for i in range(n-1):
            # if timeSeries[i] + duration < timeSeries[i + 1]:
            #     ans += duration
            # else:
            #     ans += timeSeries[i+1] - timeSeries[i]
            ans += min(timeSeries[i+1] - timeSeries[i], duration)
        ans += duration
        return ans