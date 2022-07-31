# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        q = [root]
        ans = 1
        cur_sum = root.val

        while q:
            new_q = []
            new_sum = 0
            for node in q:
                if node.left:
                    new_q.append(node.left)
                    new_sum += node.left.val

                if node.right:
                    new_q.append(node.right)
                    new_sum += node.right.val

            level += 1
            if new_sum > cur_sum and len(new_q) > 0:
                ans = level
                cur_sum = new_sum

            q = new_q

            # print(level, new_sum)

        return ans
