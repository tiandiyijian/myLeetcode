class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, depth):
            if not node:
                self.ans = max(self.ans, depth)
                return
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        self.ans = 0
        dfs(root, 0)
        return self.ans
    
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth2(TreeNode(0)))