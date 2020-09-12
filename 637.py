import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        q = collections.deque()
        q.appendleft(root)
        while q:
            tmp_len = len(q)
            layer_sum = 0
            for _ in range(tmp_len):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                layer_sum += node.val
            ans.append(layer_sum / tmp_len)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
