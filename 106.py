from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        def helper(start, end):
            if start > end:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = inorder.index(val)
            root.right = helper(index+1, end)
            root.left = helper(start, index-1)
            return root

        return helper(0, len(inorder) - 1)
    
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(i1, i2, p1, p2):
            if i1 > i2:
                return None
            root = TreeNode(postorder[p2])
            root_idx = inorder.index(postorder[p2])
            root.left = build(i1, root_idx - 1, p1, p1 + root_idx - i1 - 1)
            root.right = build(root_idx + 1, i2, p1 + root_idx - i1, p2 - 1)
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
        