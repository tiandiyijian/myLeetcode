from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        size = len(nums)
        if size & 1 == 0:
            return True
        dp = nums[:]
        for i in range(size-2, -1, -1):
            for j in range(i + 1, size):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[size-1] >= 0


if __name__ == "__main__":
    s = Solution()
    print()
