# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isIdentical(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and self.isIdentical(node1.left, node2.left) and self.isIdentical(node1.right, node2.right)
        elif node1 or node2:
            return False
        else:
            return True

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = []
        node = s
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            tmp = stack.pop()
            if self.isIdentical(tmp, t):
                return True
            tmp = tmp.right
        return False


if __name__ == "__main__":
    s = Solution()
    print()
