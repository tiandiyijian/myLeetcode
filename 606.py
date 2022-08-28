import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        ans = ''
        stack = collections.deque([root])
        while stack:
            tmp = stack.pop()
            if isinstance(tmp, str):
                ans += tmp
            else:
                ans += str(tmp.val)
                if tmp.right:
                    stack.append(')')
                    stack.append(tmp.right)
                    stack.append('(')
                
                if tmp.left:
                    stack.append(')')
                    stack.append(tmp.left)
                    stack.append('(')
                elif tmp.right:
                    stack.append('()')

        return ans

root = TreeNode(1)
root.left = TreeNode(2, left=TreeNode(4))
root.right = TreeNode(3)

print(Solution().tree2str(root))