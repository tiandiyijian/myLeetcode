from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[-1] < target or nums[0] > target:
            return [-1, -1]

        def bin_search(lower):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) >> 1
                if nums[mid] > target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    if lower:
                        r = mid
                    else:
                        l = mid + 1
            return l

        left = bin_search(True)
        right = bin_search(False)
        if nums[left] != target:
            return [-1, -1]
        return [left, right - 1 if nums[right] > target else right]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[-1] < target or nums[0] > target:
            return [-1, -1]

        left = bisect_left(nums, target)
        if nums[left] != target:
            return [-1, -1]

        right = bisect_right(nums, target)
        return [left, right - 1]


if __name__ == "__main__":
    s = Solution()
    print()
