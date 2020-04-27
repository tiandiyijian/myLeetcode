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