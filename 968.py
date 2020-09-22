# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            # a是该节点放置监控所需的最小监控数
            # b是该节点及其子节点都被监控到所需的最小监控数，本身不一定放置
            # c是该节点的子节点都被监控到所需的最小监控数，本身不一定放置
            if not node:
                return float('inf'), 0, 0
            la, lb, lc = dfs(node.left)
            ra, rb, rc = dfs(node.right)
            a = lc + rc + 1
            b = min(a, min(la + rb, lb + ra))
            c = min(a, lb + rb)
            return a, b, c

        return dfs(root)[1]


if __name__ == "__main__":
    s = Solution()
    print()
