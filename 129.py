class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is not None:
            self.res = 0
            def calculateSum(root, currentSum):
                if root.left is None and root.right is None:
                    self.res += currentSum * 10 + root.val
                else:
                    if root.left is not None:
                        calculateSum(root.left, currentSum * 10 + root.val)
                    if root.right is not None:
                        calculateSum(root.right, currentSum * 10 + root.val)
            calculateSum(root, 0)
            return self.res
        else:
            return 0