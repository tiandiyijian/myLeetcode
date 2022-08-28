from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        indices = {v: i for i, v in enumerate(arr)}
        dp = [[0] * n for _ in range(n)]
        ans = 0

        # dp[j][i] 表示以下标j和i为结尾的斐波纳挈序列的最大长度
        for i in range(2, n):
            for j in range(i - 1, 0, -1):
                pre = arr[i] - arr[j]
                if pre >= arr[j]:
                    break
                if pre not in indices:
                    continue
                k = indices[pre]
                dp[j][i] = max(3, dp[j][i], dp[k][j] + 1)
                ans = max(dp[j][i], ans)

        # print('\n'.join(str(row) for row in dp))
        return ans


arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [2,4,7,8,9,10,14,15,18,23,32,50]
arr = [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34]
print(Solution().lenLongestFibSubseq(arr))
