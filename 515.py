from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = [root]
        while q:
            curMax = float('-inf')
            newQ = []
            for node in q:
                curMax = max(curMax, node.val)
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
            ans.append(curMax)
            q = newQ

        return ans
