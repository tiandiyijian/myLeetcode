# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            nonlocal total_tilt
            total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum
        
        dfs(root)
        return total_tilt