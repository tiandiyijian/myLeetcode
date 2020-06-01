from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # ans = [False] * len(candies)
        max_candies = max(candies)
        ans = [True if c + extraCandies >=
               max_candies else False for c in candies]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))
