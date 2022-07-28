from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr1 = sorted(arr)
        ans = [0] * n
        mp = {}
        idx = 1
        mp[arr1[0]] = idx
        for i in range(1, n):
            if arr1[i] > arr1[i - 1]:
                idx += 1
                mp[arr1[i]] = idx

        for i in range(n):
            ans[i] = mp[arr[i]]

        return ans
