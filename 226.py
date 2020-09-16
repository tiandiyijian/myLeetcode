class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # right = root.right
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        # root.left = self.invertTree(right)
        return root


if __name__ == "__main__":
    s = Solution()
    print()
