from typing import List

from typing import List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans = []
        l = []
        cur_sum = 0

        def dfs(root):
            if not root:
                return
            nonlocal cur_sum
            cur_sum += root.val
            l.append(root.val)

            if not root.left and not root.right:
                if cur_sum == target:
                    ans.append(l[:])
                cur_sum -= root.val
                l.pop()
                return

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            cur_sum -= root.val
            l.pop()

        dfs(root)
        return ans