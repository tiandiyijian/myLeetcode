from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = [root]
        tem = root
        while stack:
            if stack[-1].left != tem and stack[-1].right != tem:#右兄
                self.goto_height_leaf_visable_from_left(stack)
            tem = stack.pop()
            res.append(tem.val)
        return res

    def goto_height_leaf_visable_from_left(self, s):
        while 1:
            node = s[-1]
            if node is None:
                break
            if node.left is not None:
                if node.right is not None:
                    s.append(node.right)
                s.append(node.left)
            else:
                s.append(node.right)
        s.pop()
    
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s = [root]
        ans = []
        while s:
            node = s.pop()
            ans.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return ans[::-1]
