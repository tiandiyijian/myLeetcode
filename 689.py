from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[[0, -1] for _ in range(n)] for _ in range(3)]
        # dp[i, j]的第一维表示前j个元素中(i+1)个不重叠子数组的最大值, 第二维表示得到该最大值的子数组的起始下标
        pre_sum = [0] * (n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        # dp[0][k-1] = [pre_sum[k], 0]
        for j in range(k-1, n):
            if (tmp := pre_sum[j+1] - pre_sum[j-k+1]) > dp[0][j-1][0]:
                dp[0][j] = [tmp, j-k+1]
            else:
                dp[0][j] = dp[0][j-1][:]
        for i in range(1, 3):
            for j in range(k*(i+1)-1, n):
                choose = dp[i-1][j-k][0] + pre_sum[j+1] - pre_sum[j-k+1]
                if choose > dp[i][j-1][0]:
                    dp[i][j] = [choose, j-k+1]
                else:
                    dp[i][j] = dp[i][j-1][:]
        # print(nums)
        # print(pre_sum)
        # print(dp[0])
        i3 = dp[2][n-1][1]
        i2 = dp[1][i3-1][1]
        i1 = dp[0][i2-1][1]
        return [i1, i2, i3]

nums =  [1,2,1,2,1,2,1,2,1]
k = 2
print(Solution().maxSumOfThreeSubarrays(nums, k))