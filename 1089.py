from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        size = 0
        for i in range(n):
            if arr[i] == 0:
                size += 2
            else:
                size += 1
            if size >= n:
                break

        r = n - 1
        if arr[i] == 0:
            if size == n:
                arr[r] = 0
                arr[r - 1] = 0
                r -= 2
            else:
                arr[r] = 0
                r -= 1
            i -= 1

        for j in range(i, -1, -1):
            if arr[j] == 0:
                arr[r] = 0
                arr[r - 1] = 0
                r -= 2
            else:
                arr[r] = arr[j]
                r -= 1
