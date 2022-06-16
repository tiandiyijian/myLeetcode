from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        pre = None
        if k == 0:
            for i in range(1, n):
                if nums[i] == nums[i - 1]:
                    if pre is None or nums[i] != pre:
                        ans += 1
                        pre = nums[i]
            return ans

        i = 0
        j = 1
        while j < n:
            if nums[j] == nums[j - 1]:
                j += 1
                continue
            while nums[j] - nums[i] > k:
                i += 1
            if nums[j] - nums[i] == k:
                ans += 1
            j += 1
        return ans


nums = [3, 1, 4, 1, 5]
k = 2
nums = [1, 3, 1, 5, 4]
k = 0
print(Solution().findPairs(nums, k))
