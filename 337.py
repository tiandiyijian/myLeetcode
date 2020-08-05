# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_with_self, left_without_self = dfs(node.left)
            right_with_self, right_without_self = dfs(node.right)
            return node.val + left_without_self + right_without_self, max(left_without_self, left_with_self) + max(
                right_without_self, right_with_self)

        return max(dfs(root))


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(s.rob(root))
