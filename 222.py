# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def exist(mid, depth):
            node = root
            while depth > 0:
                depth -= 1
                node = node.right if (1 << depth) & mid else node.left
            return node is not None

        if not root:
            return 0
        depth = -1
        tmp = root
        while tmp:
            depth += 1
            tmp = tmp.left
        low = 0
        high = (1 << depth) - 1
        while low < high:
            mid = (low + high + 1) >> 1
            if exist(mid, depth):
                low = mid
            else:
                high = mid - 1
        # print(low, high)
        return 2 ** depth - 1 + low + 1


if __name__ == "__main__":
    s = Solution()
    print()
