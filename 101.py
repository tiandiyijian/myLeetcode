# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = collections.deque([root.left, root.right])
        while q:
            a = q.pop()
            b = q.pop()
            if not a and not b:
                continue
            if a and b:
                if a.val == b.val:
                    q.appendleft(a.left)
                    q.appendleft(b.right)
                    q.appendleft(a.right)
                    q.appendleft(b.left)
                else:
                    return False
            else:
                return False
        return True