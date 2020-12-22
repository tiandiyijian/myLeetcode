from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        l2r = True
        while q:
            current_len = len(q)
            tmp = [None] * current_len
            if l2r:
                for i in range(current_len):
                    node = q.popleft()
                    tmp[i] = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            else:
                for i in range(current_len):
                    node = q.pop()
                    tmp[i] = node.val
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            l2r = not l2r
            ans.append(tmp)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
