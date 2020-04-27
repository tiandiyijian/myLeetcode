from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            # lt, rt, rd, ld = (i, i), (i, n-1-i), (n-1-i, n-1-i), (n-1-i, i)
            print(i)
            tmp = matrix[i][i: n-i]
            offset = 0
            for j in range(i, n-1-i):
                print(f'{matrix[i][j]} -> {matrix[n-i-1-offset][i]}')
                matrix[i][j] = matrix[n-i-1-offset][i]
                offset += 1
            print('---')
            for j in range(i+1, n-i):
                print(f'{matrix[j][i]} -> {matrix[n-i-1][j]}')
                matrix[j][i] = matrix[n-i-1][j]
            print('---')
            offset = 1
            for j in range(i+1, n-i):
                # print(j)
                print(f'{matrix[n-i-1][j]} -> {matrix[n-i-1-offset][n-i-1]}')
                matrix[n-i-1][j] = matrix[n-i-1-offset][n-i-1]
                offset += 1
            print('---')
            offset = 0
            for j in range(i, n-i-1):
                print(f'{matrix[i + j][n-i-1]} -> {tmp[offset]}')
                matrix[j][n-i-1] = tmp[offset]
                offset += 1
            print(matrix)
        return matrix


if __name__ == "__main__":
    s = Solution()
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    l = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print(s.rotate(l))
