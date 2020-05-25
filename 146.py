class Node:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key
    
    def __repr__(self):
        return f'{self.key}:{self.val}'


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.m.get(key, None)
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.addToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
            # self.head.next, self.head.next.prev, node.prev, node.next = node, node, self.head, self.head.next
            self.addToHead(node)
        else:
            if len(self.m) == self.capacity:
                node_to_delete = self.tail.prev
                node_to_delete.prev.next = node_to_delete.next
                node_to_delete.next.prev = node_to_delete.prev
                self.m.pop(node_to_delete.key)
                del node_to_delete
            node = Node(key, value)
            node.prev, node.next, self.head.next.prev, self.head.next = self.head, self.head.next, node, node
            # self.addToHead(node)
            self.m[key] = node

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(5)
    # param_1 = obj.get(1)
    # obj.put(1, 1)
    # print(obj.get(1))
    import IPython; IPython.embed()