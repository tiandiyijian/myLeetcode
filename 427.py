from typing import List


# Definition for a QuadTree node.
class Node:

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft,
                 bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':
        if self.checkgrid(grid):
            return Node(grid[0][0], 1, None, None, None, None)

        n = len(grid)
        # root = Node(0, 0)
        half = n >> 1
        topGrid = grid[:half]
        topLeftGrid = [row[:half] for row in topGrid]
        topRightGrid = [row[half:] for row in topGrid]

        bottomGrid = grid[half:]
        bottomLeftGrid = [row[:half] for row in bottomGrid]
        bottomRightGrid = [row[half:] for row in bottomGrid]

        return Node(0, 0, self.construct(topLeftGrid),
                    self.construct(topRightGrid),
                    self.construct(bottomLeftGrid),
                    self.construct(bottomRightGrid))

    def checkgrid(self, grid) -> bool:
        # 其实只传递左上角和右下角的坐标就行了
        # 不过测试样例较小也可以过
        # 还可以用前缀和优化
        n = len(grid)
        if n == 1:
            return True
        val = grid[0][0]
        for row in grid:
            for v in row:
                if v != val:
                    return False
        return True