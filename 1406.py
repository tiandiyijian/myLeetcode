from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # suffix_sum = [0] * (n + 1)
        # for i in range(n-1, -1, -1):
        #     suffix_sum[i] = suffix_sum[i+1] + stoneValue[i]
        dp = [0] * (n+1)
        suffix_sum = 0
        for i in range(n-1, -1, -1):
            suffix_sum += stoneValue[i]
            dp[i] = suffix_sum - min(dp[i+1:i+4])

        if (tmp := dp[0] << 1) == suffix_sum:
            return "Tie"
        elif tmp > suffix_sum:
            return "Alice"
        else:
            return "Bob"
