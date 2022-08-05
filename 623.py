from collections import deque
from pyparsing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        q = [root]
        
        for _ in range(1, depth-1):
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        
        for node in q:
            # if node.left:
            node.left = TreeNode(val, node.left)
            # if node.right:
            node.right = TreeNode(val, right=node.right)
        
        return root
                