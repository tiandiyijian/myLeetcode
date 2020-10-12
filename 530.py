# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float('inf')
        pre_value = float('-inf')

        def helper(node):
            if not node:
                return
            nonlocal ans, pre_value
            helper(node.left)
            ans = min(ans, node.val - pre_value)
            pre_value = node.val
            helper(node.right)

        helper(root)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
