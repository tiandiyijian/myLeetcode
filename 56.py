from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = [intervals[0][:]]
        idx = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[idx][1]:
                ans[idx][1] = max(intervals[i][1], ans[idx][1])
            else:
                ans.append(intervals[i][:])
                idx += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    l = [[1,7],[2,6],[8,10],[15,18]]
    # l = [[1,4],[4,5]]
    # l = []
    print(s.merge(l))