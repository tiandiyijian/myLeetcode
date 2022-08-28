from functools import reduce
from typing import List
import heapq

class Solution:
    def maximumProduct1(self, nums: List[int], k: int) -> int:
        # 并不能用DP
        mod = 10 ** 9 + 7
        n = len(nums)
        all = sum(nums) + k
        mean = all / n
        print(all, mean)
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0] = [1] * (k+1)
        for i in range(1, n+1):
            for j in range(k+1):
                for w in range(j+1):
                    dp[i][j] = max(dp[i][j] % mod, dp[i-1][j-w] * (nums[i-1] + w) % mod)
        print(dp)
        return dp[n][k]
    
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # 每一次操作能够带来的最大收益是别的所有数字的乘积
        # 所以要选择最小的数字来操作
        # 因为这样收益才是最大的
        mod = 10 ** 9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums, nums[0]+1)
        return reduce(lambda x, y: x * y % mod, nums)


nums = [24,5,64,53,26,38]
k = 54
print(Solution().maximumProduct(nums, k))
