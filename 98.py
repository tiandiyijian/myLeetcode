# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.values = []
        self.valid = True
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.valid and root.val < self.values[-1]:
                self.valid = False
                return
            self.values.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.valid

if __name__ == "__main__":
    s = Solution()
    print()