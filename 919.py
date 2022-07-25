from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.last_nodes = deque()
        # self.next_layer = []

        q = [root]
        for node in q:
            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)
            elif node.left:
                q.append(node.left)
                self.last_nodes.append(node)
            else:
                self.last_nodes.append(node)

    def insert(self, val: int) -> int:
        node = self.last_nodes[0]
        new_node = TreeNode(val)

        if node.left:
            node.right = new_node
            self.last_nodes.popleft()
        else:
            node.left = new_node
        self.last_nodes.append(new_node)

        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
