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

    def inorderTraversal2(self, root):
        ans = []
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right
                if pre.right is root:
                    ans.append(root.val)
                    pre.right = None
                    root = root.right
                else:
                    pre.right = root
                    root = root.left
            else:
                ans.append(root.val)
                root = root.right
        return ans    
