from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 直接给每层的node编号
        ans = 1
        q = [[root, 0]]
        while q:
            ans = max(ans, q[-1][1] - q[0][1]+1)

            new_q = []
            for node, index in q:
                if node.left:
                    new_q.append([node.left, index<<1])
                if node.right:
                    new_q.append([node.right, (index << 1) + 1])
            
            q = new_q
        return ans