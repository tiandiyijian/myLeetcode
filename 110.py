# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return max(left, right) + 1
        
        dfs(root)
        return self.ans



if __name__ == "__main__":
    s = Solution()
    print()