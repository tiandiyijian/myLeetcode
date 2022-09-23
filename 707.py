class MyLinkedList:
    class Node:
        def __init__(self, x):
            self.val = x
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length == 0:
            return -1
        if index >= self.length or index < 0:
            return -1
        print(self.length, ' ', index)
        thead = self.head
        for i in range(index):
            thead = thead.next
        return thead.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.length > 0:
            thead = self.Node(val)
            thead.next = self.head
            self.head.prev = thead
            self.head = thead
        elif self.length == 0:
            self.head = self.Node(val)
            self.tail = self.head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.length > 0:
            newTail = self.Node(val)
            newTail.prev = self.tail
            self.tail.next = newTail
            self.tail = newTail
        elif self.length == 0:
            self.tail = self.Node(val)
            self.head = self.tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif 0 < index < self.length:
            cur = self.head
            for i in range(index):
                cur = cur.next
            prevOfCur = cur.prev
            newNode = self.Node(val)
            newNode.prev = prevOfCur
            newNode.next = cur
            prevOfCur.next = newNode
            cur.prev = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.length:
            if index == 0:
                self.head = self.head.next
                if self.length == 1:
                    self.tail = self.head
            elif index == self.length - 1:
                self.tail = self.tail.prev
                if self.length == 1:
                    self.head = self.tail
            else:
                thead = self.head
                for i in range(index):
                    thead = thead.next
                thead.prev.next = thead.next
                thead.next.prev = thead.prev
            self.length -= 1


class Node:
    def __init__(self, val=-1, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class MyLinkedList2:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prv = self.head
        self.size = 0

    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node else -1

    def getNode(self, index: int) -> Node:
        if index >= self.size:
            return None
        cur = self.head.nxt
        for _ in range(index):
            cur = cur.nxt
        return cur

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head, self.head.nxt)
        self.head.nxt.prv = node
        self.head.nxt = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail.prv, self.tail)
        self.tail.prv.nxt = node
        self.tail.prv = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return

        insert_node = self.getNode(index)
        if insert_node is None:
            return

        node = Node(val, insert_node.prv, insert_node)
        insert_node.prv.nxt = node
        insert_node.prv = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        delete_node = self.getNode(index)
        if delete_node is not None:
            delete_node.prv.nxt, delete_node.nxt.prv = delete_node.nxt, delete_node.prv
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtIndex(1, 2)
    obj.get(1)
    obj.get(0)
    obj.get(2)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
