from typing import List


class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        missing_sum = mean * (m + n) - sum(rolls)
        if missing_sum > 6 * n or missing_sum < n:
            return []

        missing_mean = missing_sum // n
        mod = missing_sum % n

        return [missing_mean] * (n - mod) + [missing_mean + 1] * mod
