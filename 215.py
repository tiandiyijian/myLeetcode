from typing import List
from random import randint


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def paration(lo, hi):
            rand_idx = randint(lo, hi)
            nums[lo], nums[rand_idx] = nums[rand_idx], nums[lo]
            pivot = nums[lo]
            while lo < hi:
                while lo < hi and nums[hi] <= pivot:
                    hi -= 1
                nums[lo] = nums[hi]
                while lo < hi and nums[lo] >= pivot:
                    lo += 1
                nums[hi] = nums[lo]
            nums[lo] = pivot
            return lo

        lo = 0
        hi = len(nums) - 1
        while True:
            mid = paration(lo, hi)
            if mid == k - 1:
                return nums[mid]
            elif mid > k - 1:
                hi = mid - 1
            else:
                lo = mid + 1


if __name__ == "__main__":
    s = Solution()
    n = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(s.findKthLargest(n, k))
