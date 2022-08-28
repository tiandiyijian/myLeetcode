from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0, 0

            left_sum, left_cnt = dfs(root.left)
            right_sum, right_cnt = dfs(root.right)

            cur_sum = left_sum + right_sum + root.val
            cur_cnt = left_cnt + right_cnt + 1
            if cur_sum // cur_cnt == root.val:
                nonlocal ans
                ans += 1

            return cur_sum, cur_cnt

        dfs(root)
        return ans