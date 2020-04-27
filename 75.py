class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 1:
                i += 1
                continue
            elif nums[i] == 0:
                self.swap(nums, l, i)
                l += 1
                i += 1
            else:
                self.swap(nums, r, i)
                r -= 1

    def swap(self, nums, i, j):
        tem = nums[i]
        nums[i] = nums[j]
        nums[j] = tem
