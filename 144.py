from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        s = []
        tem = root
        while 1:
            self.visit_along_left(s, tem, res)
            if not s:
                break
            tem = s.pop().right
        return res

    def visit_along_left(self, stack, root, res):
        while root is not None:
            stack.append(root)
            res.append(root.val)
            root = root.left

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        ans = []
        node = root
        while node:
            if not node.left:
                ans.append(node.val)
                node = node.right
            else:
                pre = node.left
                while pre.right and pre.right is not node:
                    pre = pre.right
                if pre.right is node:
                    pre.right = None
                    node = node.right
                else:
                    pre.right = node
                    ans.append(node.val)
                    node = node.left
        return ans
