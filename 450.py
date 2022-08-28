from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        dummy = TreeNode(-1, root)

        def dfs(father: TreeNode, cur: TreeNode):
            if not cur:
                return
            if cur.val == key:
                if cur.right:
                    replace = cur.right
                    tmp = replace
                    while tmp.left:
                        tmp = tmp.left
                    tmp.left = cur.left
                else:
                    replace = cur.left

                if father.left is cur:
                    father.left = replace
                else:
                    father.right = replace
                return
            elif cur.val > key:
                dfs(cur, cur.left)
            else:
                dfs(cur, cur.right)

        dfs(dummy, root)
        return dummy.left
