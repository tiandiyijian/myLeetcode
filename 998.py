from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val < val:
            return TreeNode(val, left=root)

        father = None
        node = root
        while node and val < node.val:
            father = node
            node = node.right

        father.right = TreeNode(val, left=father.right)
        return root
