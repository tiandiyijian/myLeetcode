from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * i for i in range(1, numRows + 1)]
        if numRows <= 2:
            return ans

        for row in range(2, numRows):
            for i in range(1, row):
                ans[row][i] = ans[row-1][i-1] + ans[row-1][i]
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
