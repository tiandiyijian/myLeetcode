# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val

        def helper(root):
            nonlocal val
            if not root:
                return True
            if root.val != val:
                return False

            return helper(root.left) and helper(root.right)

        return helper(root)
