from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = collections.deque([root])
        ans = []
        while q:
            length = len(q)
            ans.append(q[0].val)
            for _ in range(length):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.rightSideView(TreeNode(233)))