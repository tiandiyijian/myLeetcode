class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        # temSum = res
        # for i in range(1, len(nums)):
        #     if nums[i] < 0:
        #         if temSum < 0:
        #             temSum = nums[i]
        #         else:
        #             temSum += nums[i]
        #     else:
        #         if temSum > 0:
        #             temSum += nums[i]
        #         else:
        #             temSum = nums[i]
        #     if temSum > res:
        #         res = temSum
        temSum = 0
        for i in nums:
            temSum += i
            if temSum > res:
                res = temSum
            if temSum < 0:
                temSum = 0
        return res