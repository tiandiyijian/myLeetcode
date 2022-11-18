from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        ans = 0
        nums.sort()
        pow = [1] * n
        for i in range(1, n):
            pow[i] = pow[i - 1] * 2 % mod

        for i in range(n):
            ans = (ans + (pow[i] - pow[n - 1 - i]) * nums[i] % mod) % mod

        return ans
