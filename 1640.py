from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        pos = [-1] * 101
        for i, num in enumerate(arr):
            pos[num] = i

        for p in pieces:
            idx = pos[p[0]]
            for num in p:
                if idx == n or num != arr[idx]:
                    return False
                idx += 1

        return True
