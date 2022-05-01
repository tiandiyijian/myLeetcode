from typing import List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, l2 = [], []

        def helper(node, l):
            if not node:
                return
            helper(node.left, l)
            l.append(node.val)
            helper(node.right, l)

        helper(root1, l1)
        helper(root2, l2)

        l = []
        i1 = i2 = 0
        s1, s2 = len(l1), len(l2)
        while i1 < s1 and i2 < s2:
            if l1[i1] < l2[i2]:
                l.append(l1[i1])
                i1 += 1
            else:
                l.append(l2[i2])
                i2 += 1
        if i1 == s1:
            l.extend(l2[i2:])
        else:
            l.extend(l1[i1:])

        return l