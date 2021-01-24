from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        while l < len(nums):
            r = l + 1
            while r < len(nums) and nums[r] > nums[r-1]:
                r += 1
            ans = max(ans, r - l)
            l = r
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
