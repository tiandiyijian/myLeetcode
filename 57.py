from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[-1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[-1] == intervals[0][0]:
            intervals[0][0] = newInterval[0]
            return intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        if newInterval[0] == intervals[-1][1]:
            intervals[-1][1] = newInterval[1]
            return intervals
        if newInterval[0] <= intervals[0][0]:
            intervals[0][0] = newInterval[0]
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                left = i
                break
            if i < len(intervals) - 1 and intervals[i][1] < newInterval[0] < intervals[i+1][0]:
                if newInterval[1] >= intervals[i+1][0]:
                    intervals[i+1][0] = newInterval[0]
                    left = i + 1
                    break
                else:
                    intervals.insert(i+1, newInterval)
                    return intervals
        # if newInterval[1] <= intervals[left][1]:
        #     return intervals
        # else:
        for i in range(left, len(intervals)):
            if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                # right = i
                intervals[left:i+1] = [[intervals[left][0], intervals[i][1]]]
                return intervals
            if i < len(intervals) - 1 and intervals[i][1] < newInterval[1] < intervals[i+1][0]:
                intervals[left:i+1] = [[intervals[left][0], newInterval[1]]]
                return intervals
        intervals[left:] = [[intervals[left][0], newInterval[1]]]
        return intervals


if __name__ == "__main__":
    s = Solution()
    print()
