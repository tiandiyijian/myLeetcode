import collections
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        dp = set()
        dp.add((0, 0, 0))
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            if a != x and b != y and c != z:
                continue
            tmp_set = set()
            for i, j, k in dp:
                p, q, u = max(i, a), max(j, b), max(k, c)
                if p == x and q == y and u == z:
                    return True
                tmp_set.add((p, q, u))
            dp = dp | tmp_set
        return False


if __name__ == "__main__":
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    s = Solution()
    print(s.mergeTriplets(triplets, target))
