from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        if len(target) == 0:
            return 0

        m = {x: i for i, x in enumerate(target)}

        d = []
        for i in range(len(arr)):
            if arr[i] not in m:
                continue

            idx = m[arr[i]]
            if not d or idx > d[-1]:
                d.append(idx)
                continue

            l = 0
            r = len(d) - 1
            while l < r:
                mid = (l + r) >> 1
                if d[mid] >= idx:
                    r = mid
                else:
                    l = mid + 1
            d[l] = idx

        return len(target) - len(d)
