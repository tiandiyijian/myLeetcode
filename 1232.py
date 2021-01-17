from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def getK(a, b):
            return float('inf') if a[0] == b[0] else (b[1] - a[1]) / (b[0] - a[0])

        k = getK(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            new_k = getK(coordinates[0], coordinates[i])
            if new_k != k:
                return False
            k = new_k
        return True


if __name__ == "__main__":
    s = Solution()
    print()
