from itertools import accumulate
from typing import List


class Solution_0:
    def largestSumOfAverages(self, A: list, K: int) -> float:
        sums = [0] * len(A)
        sums[0] = A[0]
        for i in range(1, len(A)):
            sums[i] = sums[i - 1] + A[i]
        dp = [[0.0] * (K + 1) for i in range(len(A))]
        for k in range(1, K + 1):
            for i in range(len(A)):
                if k == 1:
                    dp[i][k] = sums[i] / (i + 1)
                elif k > i + 1:
                    continue
                else:
                    for j in range(k - 1, i + 1):
                        dp[i][k] = max(
                            dp[i][k],
                            dp[j - 1][k - 1] + (sums[i] - sums[j - 1]) / (i - j + 1),
                        )
        print(dp)
        return dp[len(A) - 1][K]


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 像这种分段的问题是应该往动态规划上想的
        # 因为对于i第k个分段只依赖于i前面的第k-1个分段
        n = len(nums)
        pre_sum = list(accumulate(nums))

        dp = [[0] * (k + 1) for _ in range(n)]
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][1] = pre_sum[i] / (i + 1)
            for j in range(2, min(i + 1, k) + 1):
                for x in range(i):
                    dp[i][j] = max(
                        dp[i][j], dp[x][j - 1] + (pre_sum[i] - pre_sum[x]) / (i - x)
                    )

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    A = [4, 1, 7, 5, 6, 2, 3]
    K = 4
    print(s.largestSumOfAverages(A, K))
