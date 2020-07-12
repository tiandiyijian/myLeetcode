from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        dp表示的是从当前位置到右下角所需要的最小初始生命值，从右下到左上进行动态规划
        如果是从左上到右下的话既要考虑当前路径和，又要考虑到当前节点的最小初始值
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = max(1, -dungeon[-1][-1] + 1)
        for i in range(n-2, -1, -1):
            dp[m-1][i] = max(1, dp[m-1][i+1] - dungeon[m-1][i])
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    d = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(s.calculateMinimumHP(d))
