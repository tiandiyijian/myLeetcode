from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        total = cheeseSlices
        if total << 1 > tomatoSlices:
            return []
        tmomto_for_big = tomatoSlices - (total << 1)
        if tmomto_for_big & 1:
            return []
        big = tmomto_for_big >> 1
        if big <= total:
            return [big, total - big]
        return []


if __name__ == "__main__":
    s = Solution()
    print()
