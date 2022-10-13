from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        curMax = -1
        for i in range(n):
            if arr[i] > curMax:
                curMax = arr[i]

            if curMax == i:
                ans += 1
                curMax = -1

        return ans
