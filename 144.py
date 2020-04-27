# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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