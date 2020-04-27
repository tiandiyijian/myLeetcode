# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        tem = root
        while 1:
            self.go_along_left(stack, tem)
            if not stack:
                break
            tem = stack.pop()
            res.append(tem.val)
            tem = tem.right

        return res

    def go_along_left(self, stack, root):
        while root:
            stack.append(root)
            root = root.left
