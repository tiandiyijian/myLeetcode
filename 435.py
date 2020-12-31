from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        select = 0
        right = float('-inf')

        for [l, r] in intervals:
            if l >= right:
                select += 1
                right = r

        return len(intervals) - select


if __name__ == "__main__":
    s = Solution()
    print()
