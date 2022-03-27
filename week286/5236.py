from typing import List


class Solution:

    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = 0
        while i + 1 < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                ans += 1
                j += 1
            i = j + 1
        # print(n, i, ans)
        return ans + 1 if i != n else ans


nums = [
    2, 6, 2, 5, 8, 9, 7, 2, 2, 5, 6, 2, 2, 0, 6, 8, 7, 3, 9, 2, 1, 1, 3, 2, 6,
    2, 4, 6, 5, 8, 4, 8, 7, 0, 4, 8, 7, 8, 4, 1, 1, 4, 0, 1, 5, 7, 7, 5, 9, 7,
    5, 5, 8, 6, 4, 3, 6, 5, 1, 6, 7, 6, 9, 9, 6, 8, 6, 0, 9, 5, 6, 7, 6, 9, 5,
    5, 7, 3, 0, 0, 5, 5, 4, 8, 3, 9, 3, 4, 1, 7, 9, 3, 1, 8, 8, 9, 1, 6, 0, 0
]
print(Solution().minDeletion(nums))