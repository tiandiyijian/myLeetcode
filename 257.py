from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return path
            if not node.left and not node.right:
                ans.append(f'{path}{node.val}')
                return
            path = f'{path}{node.val}->'
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, '')
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
