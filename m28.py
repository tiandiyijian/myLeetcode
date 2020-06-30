from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q1 = deque([root])
        q2 = deque([root])
        while q1 and q2:
            n1, n2 = q1.pop(), q2.pop()
            if n1 and n2:
                if n1.val == n2.val:
                    q1.appendleft(n1.left)
                    q1.appendleft(n1.right)
                    q2.appendleft(n2.right)
                    q2.appendleft(n2.left)
                else:
                    return False
            elif not n1 and not n2:
                continue
            else:
                return False
        return True