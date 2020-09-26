from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        def dfs(node, path, rest):
            if not node.left and not node.right:
                if node.val == rest:
                    path.append(node.val)
                    ans.append(path)
            if node.left:
                dfs(node.left, path + [node.val], rest - node.val)
            if node.right:
                dfs(node.right, path + [node.val], rest - node.val)

        dfs(root, [], sum)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
