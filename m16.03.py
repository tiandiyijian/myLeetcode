from typing import List

class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        if start1[0] < end1[0]:
            left1, right1 = start1, end1
        else:
            left1, right1 = end1, start1
        if start2[0] < end2[0]:
            left2, right2 = start2, end2
        else:
            left2, right2 = end2, start2
        if right1[0] < left2[0] or right2[0] < left1[0]:
            return []
        elif right1[0] == left2[0]:
            return [float(right1[0]), float(right1[1])] if right1[1] == left2[1] else []
        elif right2[0] == left1[0]:
            return [float(right2[0]), float(right2[1])] if right2[1] == left1[1] else []
        


if __name__ == "__main__":
    s = Solution()
    print()