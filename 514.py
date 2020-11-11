from typing import List
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(key), len(ring)
        dp = [[float('inf')] * n for _ in range(m)]

        char_idx = defaultdict(list)
        for i, char in enumerate(ring):
            char_idx[char].append(i)

        for k in char_idx[key[0]]:
            dp[0][k] = min(k, n - k) + 1
        
        for i in range(1, m):
            for j in char_idx[key[i]]:
                for k in char_idx[key[i-1]]:
                    dp[i][j] = min(dp[i][j], 1 + dp[i-1][k] + min(abs(j-k), n - abs(j-k)))

        # for r in dp:
        #     print(r)
        return min(dp[-1])

if __name__ == "__main__":
    s = Solution()
    ring = "rtmdx"
    key =  "dmrtx"
    print(s.findRotateSteps(ring, key))