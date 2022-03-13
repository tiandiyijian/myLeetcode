from typing import List


class Solution:

    def findKDistantIndices(self, nums: List[int], key: int,
                            k: int) -> List[int]:
        n = len(nums)
        diff = [0] * (n + 1)
        for j, val in enumerate(nums):
            if val == key:
                diff[max(0, j - k)] += 1
                diff[min(n, j + k + 1)] -= 1

        ans = []
        pre_sum = 0
        for i in range(n):
            pre_sum += diff[i]
            if pre_sum > 0:
                ans.append(i)
        return ans