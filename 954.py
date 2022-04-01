from collections import defaultdict
from typing import List


class Solution:

    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=abs)
        mp = defaultdict(int)
        n = len(arr)
        i = 0
        if arr[0] == 0:
            while i < n and arr[i] == 0:
                i += 1
            if i & 1 == 1:
                return False
        # print(i, n, arr)
        for j in range(i, n):
            if mp[arr[j]] > 0:
                mp[arr[j]] -= 1
            else:
                mp[arr[j]<<1] += 1
            # print(mp)
        return all(v == 0 for v in mp.values())


print(Solution().canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2]))
