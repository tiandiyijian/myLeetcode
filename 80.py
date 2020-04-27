class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = 1
        same_num = 1
        for i in range(1, len(nums)):
            if same_num < 2 and nums[i] == nums[i-1]:
                nums[length] = nums[i]
                same_num += 1
                length += 1
            elif same_num < 2 and nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length +=1
                same_num = 1
            elif same_num >= 2 and nums[i] == nums[i-1]:
                same_num += 1
            elif same_num >= 2 and nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length += 1
                same_num = 1
        return length
