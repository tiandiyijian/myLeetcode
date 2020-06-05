from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = [None] * (m*n)
        idx = 0
        layer = 0
        total_layer = (min(m, n) + 1) // 2
        while layer < total_layer:
            for i in range(layer, n - layer):
                ans[idx] = matrix[layer][i]
                idx += 1
            for i in range(layer + 1, m - layer):
                ans[idx] = matrix[i][n - layer - 1]
                idx += 1
            if layer != m - layer - 1:
                for i in reversed(range(layer, n - layer - 1)):
                    # print(m - layer - 1, i, matrix[m - layer - 1][i])
                    ans[idx] = matrix[m - layer - 1][i]
                    idx += 1
            if layer != n - 1 - layer:
                for i in reversed(range(layer + 1, m - layer - 1)):
                    ans[idx] = matrix[i][layer]
                    idx += 1
            layer += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(matrix))
