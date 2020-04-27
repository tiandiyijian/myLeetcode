import copy
class Solution:
    def maxCoins(self, nums: list) -> int:
        if not nums:
            return 0
        # def f(nums):
        #     if not nums:
        #         return 0
        #     if len(nums) == 1:
        #         return nums[0]
        #     maxValue = 0
        #     for i in range(len(nums)):
        #         tem = nums[i]
        #         temNums = copy.deepcopy(nums)
        #         nums.pop(i)
        #         if 0 < i < len(temNums)-1:
        #             res = temNums[i-1] * temNums[i] * temNums[i+1] + f(nums)
        #         elif i == 0:
        #             res = temNums[i] * temNums[i+1] + f(nums)
        #         else:
        #             res = temNums[i-1] * temNums[i] + f(nums)
        #         nums.insert(i, tem)
        #         maxValue = max(res, maxValue)
        #     return maxValue
        # return f(nums)
        length = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        dp = [[0] * (length+2) for _ in range(length+2)]
        for size in range(1, length+1):
            for i in range(1, length-size+1+1):
                j = i + size - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])
                for i in range(len(dp[0])):
                    print(dp[i])
                print()
        return dp[1][length]

if __name__ == '__main__':
    s = Solution()
    nums = [3,1,5]
    print(s.maxCoins(nums))