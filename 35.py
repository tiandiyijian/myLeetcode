import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect.bisect_left(nums, target)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if nums[lo] < target:
            return lo + 1
        return lo

if __name__ == "__main__":
    s = Solution()
    l = [1,3,5,6]
    target = 0
    print(s.searchInsert(l, target))