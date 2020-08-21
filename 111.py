import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        current_depth = 1
        while q:
            length = len(q)
            for i in range(length):
                node = q.pop()
                if not node.left and not node.right:
                    return current_depth
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            current_depth += 1


if __name__ == "__main__":
    s = Solution()
    print()
