class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moveDirs = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1.0
        print(dp)
        for step in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for row in range(N):
                for col in range(N):
                    if dp[row][col] > 0:
                        for mr, mc in moveDirs:
                            newRow = row + mr
                            newCol = col + mc
                            if 0 <= newRow < N and 0 <= newCol < N:
                                dp2[newRow][newCol] += dp[row][col] / 8.0
            dp = dp2
            print(dp)
        #print(dp)
        return sum(map(sum, dp))

if __name__ == '__main__':
    s = Solution()
    print(s.knightProbability(3,2,0,0))