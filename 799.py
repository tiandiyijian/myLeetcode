from bisect import bisect_left
from itertools import accumulate


# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         glasses = list(range(1, 101))
#         glasses = list(accumulate(glasses))
#         row = bisect_left(glasses, poured)
#         if row >= 100:
#             return 1.0
#         if poured < glasses[row]:
#             row -= 1
#         print(row, glasses)

#         if query_row <= row:
#             return 1.0

#         if query_row > row + 1:
#             return 0.0

#         poured -= glasses[row]
#         if poured == 0:
#             return 0.0
#         row_glasses = row + 2
#         tot = (row_glasses - 2) * 2 + 2
#         print(row, poured, tot)
#         if query_glass == 0 or query_glass == row + 1:
#             return poured * 1.0 / tot
#         else:
#             return poured * 2.0 / tot


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0.0

        dp = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured
        for i in range(1, query_row + 1):
            for j in range(query_row + 1):
                if j < i:
                    dp[i][j] += max(dp[i - 1][j] - 1, 0) / 2
                if j > 0:
                    dp[i][j] += max(dp[i - 1][j - 1] - 1, 0) / 2
        # print(dp)
        return min(dp[query_row][query_glass], 1.0)


print(Solution().champagneTower(25, 6, 1))
