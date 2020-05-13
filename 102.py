from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = collections.deque([root])
        while q:
            length = len(q)
            tmp = []
            for _ in range(length):
                node = q.pop()
                tmp.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            ans.append(tmp[:])
        return ans


if __name__ == "__main__":
    s = Solution()
    print()