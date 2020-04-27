class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def legalSubTree(node: TreeNode):
            if node is None:
                return False
            if node.val == 1:
                return True
            else:
                return legalSubTree(node.left) or legalSubTree(node.right)
        if not legalSubTree(root):
            return None
        nodes = [root]
        while len(nodes) > 0:
            nextNodes = []
            for node in nodes:
                if node.left is not None and not legalSubTree(node.left):
                    node.left = None
                if node.right is not None and not legalSubTree(node.right):
                    node.right = None
                if node.left is not None:
                    nextNodes.append(node.left)
                if node.right is not None:
                    nextNodes.append(node.right)
                nodes = nextNodes
        return root