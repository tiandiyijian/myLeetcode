from typing import List


class Solution:

    def maxRotateFunction(self, nums: List[int]) -> int:
        # 递推公式可以得到
        # F(k+1) = F(k) + sum(nums) - n*nums[n-1-k]
        # 递推过程如图https://s2.loli.net/2022/04/22/hodq1vVSAKMFTzZ.png
        n = len(nums)
        Sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        ans = f
        for k in range(n - 1):
            f = f + Sum - n * nums[n - 1 - k]
            ans = max(f, ans)
        return ans