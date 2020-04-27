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
