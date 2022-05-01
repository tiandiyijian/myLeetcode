from typing import List


class Solution:

    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = {}
        n = len(cards)
        ans = n + 1
        for i, num in enumerate(cards):
            if num in mp:
                ans = min(ans, i - mp[num] + 1)
            mp[num] = i
        if ans > n:
            return -1
        return ans