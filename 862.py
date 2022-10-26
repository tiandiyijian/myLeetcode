from collections import deque
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf
        pre_s = list(accumulate(nums, initial=0))

        q = deque()
        for i, cur_s in enumerate(pre_s):
            while q and cur_s - pre_s[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and cur_s < pre_s[q[-1]]:
                q.pop()
            q.append(i)

        return ans if ans < inf else -1
