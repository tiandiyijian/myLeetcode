from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        la = len(A)
        lb = len(B)
        ans = 0
        dp = [0] * (lb + 1)
        for i in range(1, la + 1):
            for j in range(lb, 0, -1):
                dp[j] = dp[j-1] + 1 if A[i-1] == B[j-1] else 0
                ans = max(ans, dp[j])
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print(s.findLength(A, B))
