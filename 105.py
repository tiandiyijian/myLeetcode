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


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(p1, p2, i1, i2):
            if p1 == p2:
                return TreeNode(preorder[p1])
            if p1 > p2 or i1 > i2:
                return None
            idx_of_root = inorder.index(preorder[p1])
            num_left = idx_of_root - i1
            num_right = i2 - idx_of_root
            node = TreeNode(preorder[p1])
            node.left = build(p1+1, p1+num_left, i1, idx_of_root-1)
            node.right = build(p2-num_right+1, p2, idx_of_root+1, i2)
            return node
        # if not preorder:
        #     return None
        return build(0, len(preorder)-1, 0, len(inorder)-1)