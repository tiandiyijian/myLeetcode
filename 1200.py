from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minDiff = float('inf')
        
        for i in range(1, len(arr)):
            if (tmp := arr[i] - arr[i - 1]) < minDiff:
                minDiff = tmp
                ans = [[arr[i - 1], arr[i]]]
            elif tmp == minDiff:
                ans.append([arr[i - 1], arr[i]])

        return ans
