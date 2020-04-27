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
