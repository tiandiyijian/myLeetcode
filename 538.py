# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        tmp = 0

        def rsl(node):  # right-self-left
            if not node:
                return
            nonlocal tmp
            rsl(node.right)
            node.val += tmp
            tmp = node.val
            rsl(node.left)
        rsl(root)
        return root


if __name__ == "__main__":
    s = Solution()
    print()
