from typing import List


class Solution:

    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        # 关键在于枚举拐点不要枚举终点

        def sub_list(a, b):
            return list(x[0] - x[1] for x in zip(a, b))

        def add_list(a, b):
            return list(x[0] + x[1] for x in zip(a, b))

        m, n = len(grid), len(grid[0])
        row_prefix = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]
        col_prefix = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                two_cnt = five_cnt = 0
                tmp = grid[i][j]
                while tmp & 1 == 0:
                    tmp >>= 1
                    two_cnt += 1
                while tmp % 5 == 0:
                    tmp //= 5
                    five_cnt += 1
                row_prefix[i + 1][j + 1][0] = row_prefix[i + 1][j][0] + two_cnt
                row_prefix[i + 1][j +
                                  1][1] = row_prefix[i + 1][j][1] + five_cnt
                col_prefix[i + 1][j + 1][0] = col_prefix[i][j + 1][0] + two_cnt
                col_prefix[i + 1][j +
                                  1][1] = col_prefix[i][j + 1][1] + five_cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                left_up = min(
                    add_list(row_prefix[i + 1][j + 1], col_prefix[i][j + 1]))
                left_bottom = min(
                    add_list(
                        row_prefix[i + 1][j + 1],
                        sub_list(col_prefix[m][j + 1],
                                 col_prefix[i + 1][j + 1])))
                right_up = min(
                    add_list(
                        sub_list(row_prefix[i + 1][n],
                                 row_prefix[i + 1][j + 1]),
                        col_prefix[i + 1][j + 1]))
                right_bottom = min(
                    add_list(
                        sub_list(row_prefix[i + 1][n],
                                 row_prefix[i + 1][j + 1]),
                        sub_list(col_prefix[m][j + 1], col_prefix[i][j + 1])))
                # print(left_up, left_bottom, right_up, right_bottom)
                ans = max(ans, left_up, left_bottom, right_up, right_bottom)
                # print(i, j, ans)

        return ans


grid = [[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21],
        [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]
print(Solution().maxTrailingZeros(grid))
