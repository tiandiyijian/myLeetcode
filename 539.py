from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(time[:2]) * 60 + int(time[3:])
                      for time in timePoints]
        timePoints.sort()
        timePoints.append(24*60 + timePoints[0])
        return min(timePoints[i] - timePoints[i-1] for i in range(1, len(timePoints)))
