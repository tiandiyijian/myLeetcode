from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum & 1:
            return False
        target = nums_sum >> 1
        max_num = max(nums)
        if max_num > target:
            return False

        length = len(nums)
        dp = [[False] * (target + 1) for _ in range(length)]
        for i in range(length):
            dp[i][0] = True
            for j in range(1, target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print()
