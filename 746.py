from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(a + cost[i - 2], b + cost[i - 1])
        return b


if __name__ == "__main__":
    s = Solution()
    print()
