import collections


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


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = ''
        q = collections.deque([root])
        while q:
            node = q.pop()
            if node:
                ans += str(node.val) + ','
                q.appendleft(node.left)
                q.appendleft(node.right)
            else:
                ans += '#,'
        print(ans)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data[0] == '#':
            return None
        val = collections.deque(data.split(','))
        tmp_nodes = collections.deque([TreeNode(int(val[0]))])
        root = tmp_nodes[0]
        val.popleft()
        while tmp_nodes:
            length = len(tmp_nodes)
            for _ in range(length):
                node = tmp_nodes.pop()
                tmp = val.popleft()
                # print(tmp, val)
                left = None if tmp == '#' else TreeNode(int(tmp))
                tmp = val.popleft()
                # print(tmp, val)
                right = None if tmp == '#' else TreeNode(int(tmp))
                node.left = left
                node.right = right
                if left:
                    tmp_nodes.appendleft(left)
                if right:
                    tmp_nodes.appendleft(right)
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
