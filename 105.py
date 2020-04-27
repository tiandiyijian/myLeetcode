from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        if len(inorder) == 1:
            return root
        position = inorder.index(preorder[0])
        leftLength = position
        root.left = self.buildTree(preorder[1:1+position], inorder[:position])
        root.right = self.buildTree(preorder[1+position:], inorder[position + 1:])
        return root