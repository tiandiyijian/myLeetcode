from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        ans = 0
        start, end = points[0]
        ans = 1
        for l, r in points:
            if start <= l <= end:
                start = l
                end = min(end, r)
            else:
                start = l
                end = r
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
