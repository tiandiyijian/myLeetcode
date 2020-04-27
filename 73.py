class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #关键之处在于用矩阵本身记录那些需要置零的行和列
        if len(matrix) == 0:
            return

        row = -1
        col = -1

        for i in range(len(matrix)):
            flag = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row = i
                    col = j
                    flag = 1
                    break
            if flag == 1:
                break
        if row == -1:
            return

        for i in range(row, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[row][j] = 0
                    matrix[i][col] = 0

        for i in range(row + 1, len(matrix)):
            # if i == row:
            #   continue
            if matrix[i][col] == 0:
                matrix[i] = [0] * len(matrix[0])

        for j in range(len(matrix[0])):
            if j == col:
                continue
            if matrix[row][j] == 0:
                for rows in matrix:
                    rows[j] = 0

        for i in range(len(matrix)):
            matrix[i][col] = 0

        for j in range(len(matrix[0])):
            matrix[row][j] = 0

