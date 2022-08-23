from typing import List


class Solution:
    def busyStudent1(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(a <= queryTime <= b for a, b in zip(startTime, endTime))

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        e = [0] * 1002
        for a, b in zip(startTime, endTime):
            e[a] += 1
            e[b+1] -= 1

        return sum(e[:queryTime+1])
