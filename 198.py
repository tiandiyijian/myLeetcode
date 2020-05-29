class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #res = 0
        # localMax = [0] * (len(nums) + 1)
        # localMax[1] = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] + localMax[i - 1] > localMax[i]:
        #         localMax[i+1] = (nums[i] + localMax[i - 1])
        #     else:
        #         localMax[i+1] = localMax[i]
        # return localMax[-1]
        localMax1 = 0
        localMax2 = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + localMax1 > localMax2:
                localMax1, localMax2 = localMax2, localMax1 + nums[i]
            else:
                localMax1 = localMax2
            #localMax1, localMax2 = localMax2, max(nums[i] + localMax1, localMax2) best
        return localMax2


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i] + nums[i], dp[i+1])
        return dp[-1]