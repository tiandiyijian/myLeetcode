from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        v1 = [p2[0] - p1[0], p2[1] - p1[1]]
        v2 = [p3[0] - p1[0], p3[1] - p1[1]]
        v3 = [p4[0] - p1[0], p4[1] - p1[1]]
        l = [v1, v2, v3]

        def norm(x):
            return x[0] ** 2 + x[1] ** 2

        l.sort(key=norm)
        v1, v2, v3 = l

        def dot(x, y):
            return [x[0] * y[0], x[1] * y[1]]

        return (
            norm(v1) == norm(v2)
            and sum(dot(v1, v2)) == 0
            and 2 * norm(v1) == norm(v3)
            and sum(dot(v1, v3)) > 0
            and [v1[0] + v2[0], v1[1] + v2[1]] == v3
        )


print(Solution().validSquare([1, 0], [-1, 0], [0, 1], [0, -1]))
