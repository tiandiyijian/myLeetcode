import sys
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def _max(root):
            if root is None:
                return -sys.maxsize
            left = max(0, _max(root.left))
            right = max(0, _max(root.right))
            self.ans = max(self.ans, root.val + left + right)
            return max(left, right) + root.val
        self.ans = -sys.maxsize
        _max(root)
        return self.ans

    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        # 两年前写的更好，这次不行
        def dfs(node):
            cur = node.val
            root_max = cur
            cur_max = cur
            if node.left:
                lmax, lroot = dfs(node.left)
                root_max = max(cur, cur + lroot)
                cur_max = max(lmax, root_max)
            
            if node.right:
                rmax, rroot = dfs(node.right)
                root_max = max(root_max, cur + rroot)
                cur_max = max(cur_max, root_max, rmax, cur + rroot + (0 if not node.left else lroot))
            return cur_max, root_max
        
        return dfs(root)[0]
