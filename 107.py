import collections
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        nodes = [root]
        while len(nodes) > 0:
            valsOfOneRow = []
            nodesOfNextRow = []
            for node in nodes:
                valsOfOneRow.append(node.val)
                if node.left is not None:
                    nodesOfNextRow.append(node.left)
                if node.right is not None:
                    nodesOfNextRow.append(node.right)
            nodes = nodesOfNextRow
            res.append(valsOfOneRow)
        return res[::-1]

    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            tmp_len = len(q)
            layer = []
            for _ in range(tmp_len):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                layer.append(node.val)
            ans.append(layer)
        return ans[::-1]    
