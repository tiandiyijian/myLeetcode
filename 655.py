# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(root):
            return 0 if not root else max(getHeight(root.left), getHeight(root.right)) + 1

        height = getHeight(root) - 1
        m = height + 1
        n = 2 ** m - 1

        ans = [[''] * n for _ in range(m)]

        def dfs(node, row, col):
            ans[row][col] = str(node.val)
            offset = 2**(height-row-1)
            if node.left:
                dfs(node.left, row+1, col-offset)
            if node.right:
                dfs(node.right, row+1, col+offset)

        dfs(root, 0, (n-1)//2)
        return ans
