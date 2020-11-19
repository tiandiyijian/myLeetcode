from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = q = 0
        m = len(nums)
        while p < m and q < m:
            while p < m and nums[p] != 0:
                p += 1
            q = max(q, p)
            while q < m and nums[q] == 0:
                q += 1
            if q < m:
                nums[p], nums[q] = nums[q], nums[p]
            p += 1


if __name__ == "__main__":
    s = Solution()
    print()
