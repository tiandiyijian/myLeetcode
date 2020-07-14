from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        storeys = len(triangle)
        for row in range(storeys-2, -1, -1):
            for col in range(row+1):
                triangle[row][col] += min(triangle[row+1]
                                          [col], triangle[row+1][col+1])
        return triangle[0][0]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [5, 6, 7]]))
