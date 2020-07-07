class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def dfs(node, tmp_sum):
            if not node:
                return False
            if not node.left and not node.right:
                if tmp_sum + node.val == sum:
                    return True
                return False
            return dfs(node.left, tmp_sum + node.val) or dfs(node.right, tmp_sum + node.val)
        return dfs(root, 0)