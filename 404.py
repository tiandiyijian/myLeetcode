class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = Noneclass Solution:


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = r = 0
        if root.left:
            l = self.sumOfLeftLeaves(root.left)
        if root.right:
            r = self.sumOfLeftLeaves(root.right)
        if root.left and (not root.left.left and not root.left.right):
            return root.left.val + r
        return l + r


if __name__ == "__main__":
    s = Solution()
    print()
