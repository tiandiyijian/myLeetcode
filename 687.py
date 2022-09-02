from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans

        def dfs(root):
            if not root:
                return 0

            nonlocal ans

            left = right = 0
            if root.left:
                left = dfs(root.left)

            if root.right:
                right = dfs(root.right)

            cur = 1
            sons = [0]
            if left > 0 and root.left.val == root.val:
                cur += left
                sons.append(left)
            if right > 0 and root.right.val == root.val:
                cur += right
                sons.append(right)

            ans = max(ans, cur)

            return 1 + max(sons)

        dfs(root)
        return ans - 1  # 节点数减一
