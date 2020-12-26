from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        width, length = len(matrix), len(matrix[0])
        left = [0] * length
        right = [length] * length
        height = [0] * length
        maxRec = 0
        for i in range(width):
            curLeft, curRight = 0, length
            for j in range(length):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], curLeft)
                else:
                    height[j] = 0
                    left[j] = 0
                    curLeft = j + 1
            for j in range(length - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curRight)
                else:
                    right[j] = length
                    curRight = j
            for j in range(length):
                maxRec = max(maxRec, (right[j] - left[j]) * height[j])
        return maxRec

    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = 1 if j == 0 else (left[i][j-1] + 1)

        max_rec = 0
        for j in range(n):
            stack = []
            i = 0
            while i <= m:
                if not stack or (i < m and left[i][j] >= left[stack[-1]][j]):
                    stack.append(i)
                    i += 1
                else:
                    height = left[stack.pop()][j]
                    width = i - 1 - stack[-1] if stack else i
                    max_rec = max(max_rec, height * width)
        return max_rec


if __name__ == "__main__":
    s = Solution()
    m = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(s.maximalRectangle2(m))
