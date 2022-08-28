from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # 对右端点降序是因为如果左端点一样的话这样后面的区间是前面的区间的子集
        # 后面的符合条件的话那么前面的也一定符合条件
        # print(intervals)
        ans = 2
        a = intervals[-1][0]
        b = a + 1
        # print(a, b)
        for i in range(len(intervals) - 2, -1, -1):
            l, r = intervals[i]
            if r >= b:
                continue
            elif r >= a:
                a, b = l, a
                ans += 1
            else:
                a, b = l, l + 1
                ans += 2
            # print(a, b)
        return ans
