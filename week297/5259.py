from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        brackets = [[0, 0]] + brackets
        n = len(brackets)
        for i in range(1, n):
            ans += (
                (min(income, brackets[i][0]) - brackets[i - 1][0])
                * brackets[i][1]
                / 100
            )
            if income <= brackets[i][0]:
                return ans
        return ans


b = [[3, 50], [7, 10], [12, 25]]
inc = 10
print(Solution().calculateTax(b, inc))
