from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i
                while j < len(nums) and nums[j] > nums[i - 1]:
                    j += 1
                j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                # nums[i:] = nums[len(nums) - 1:i-1:-1]
                nums[i:] = reversed(nums[i::])
                return
            i -= 1
        for i in range(len(nums) // 2):
            nums[i], nums[-(i + 1)] = nums[-(i + 1)], nums[i]


if __name__ == "__main__":
    s = Solution()
    print()
