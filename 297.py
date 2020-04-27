class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.nodes = ''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            self.nodes += '#,'
        else:
            self.nodes += (str(root.val) + ',')
            self.serialize(root.left)
            self.serialize(root.right)
        return self.nodes


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.listOfNodes = data.split(',')
        def deserialize(listOfNodes):
            val = listOfNodes.pop(0)
            if val == '':
                return
            else:
                if val == '#':
                    return None
                val = int(val)
                root = TreeNode(val)
                left = deserialize(listOfNodes)
                right = deserialize(listOfNodes)
                root.left = left
                root.right = right
                return root
        root = deserialize(self.listOfNodes)
        return root

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    s = Codec()
    root = s.deserialize(s.serialize(a))
    print(root.val, root.left.val, root.right.val)
