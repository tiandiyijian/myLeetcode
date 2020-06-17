from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = A[0]
        left = ans
        for j in range(1, len(A)):
            ans = max(left + A[j] - j, ans)
            left = max(left, A[j] + j)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
