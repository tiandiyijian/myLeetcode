from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 直接DFS的复杂度是4的n次方, 因为每个火柴都有四种分配的可能性
        # 但是其实每个火柴只有已经被选中了和没有被选中两种可能性, 同时记录已经选中的火柴的总长度即可
        # 这样就把复杂度降到了n乘2的n次方

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        edge = total // 4
        if any(stick > edge for stick in matchsticks):
            return False

        n = len(matchsticks)
        dp = [-1] * (1 << n)
        dp[0] = 0
        for state in range(1, len(dp)):
            for i, v in enumerate(matchsticks):
                if state & (1 << i) == 0:
                    continue
                pre_state = state & ~(1 << i)
                if dp[pre_state] >= 0 and dp[pre_state] + v <= edge:
                    dp[state] = (dp[pre_state] + v) % edge
                    break
        return dp[-1] == 0
