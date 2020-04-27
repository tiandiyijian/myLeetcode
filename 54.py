currentCol = 0
currentRow = 0


def add(list, count, dir, matrix):
    global currentRow
    global currentCol
    row = currentRow
    col = currentCol
    if dir == 0:
        while col < currentCol + count:
            list.append(matrix[row][col])
            col += 1
        currentRow += 1
        currentCol = col - 1
    elif dir == 1:
        while row < currentRow + count:
            list.append(matrix[row][col])
            row += 1
        currentRow = row - 1
        currentCol -= 1
    elif dir == 2:
        while col > currentCol - count:
            list.append(matrix[row][col])
            col -= 1
        currentRow -= 1
        currentCol = col + 1
    elif dir == 3:
        while row > currentRow - count:
            list.append(matrix[row][col])
            row -= 1
        currentRow = row + 1
        currentCol += 1


class Solution:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # cols = len(matrix[0])
        # rows = len(matrix)
        # res = []
        # # append
        # dir = 0
        # count = cols
        # while count > 0:
        #     add(res, count, dir, matrix)
        #     if dir == 0 | dir == 2:
        #         rows -= 1
        #         count = rows
        #     else:
        #         cols -= 1
        #         count = cols
        #     dir = (dir + 1) % 4
        # return res

        rows = len(matrix)
        if rows < 1: return []
        cols = len(matrix[0])
        if cols < 0: return []
        tmp = min(rows, cols)
        layer = tmp // 2 + (1 if tmp % 2 == 1 else 0)
        print(rows, cols)
        ans = []
        for i in range(layer):
            # print(i)
            ans += matrix[i][i : cols - i]
            print(ans)
            for j in range(i + 1, rows - i):
                ans.append(matrix[j][cols - i - 1])
            print(ans)
            if rows - 1 - i == i: break #最后一层只有一行
            ans += matrix[rows - 1 - i][cols - i - 2 : i : -1]
            print(ans)
            if i == cols - i - 1: break #最后一层只有一列
            for j in range(rows - 1 - i, i, -1):
                ans.append(matrix[j][i])
        return ans


if __name__ == "__main__":
    s = Solution()
    # l = [[1,2,3],[4,5,6],[7,8,9]]
    l = [[3,2,4]]
    print(s.spiralOrder(l))