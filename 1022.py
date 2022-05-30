# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, curVal):
            curVal = (curVal << 1) + root.val
            if root.left:
                dfs(root.left, curVal)
            if root.right:
                dfs(root.right, curVal)
            if not root.left and not root.right:
                nonlocal ans
                ans += curVal

        dfs(root, 0)
        return ans
