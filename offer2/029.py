# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head

        if head.next is head:
            head.next = Node(insertVal, head)
            return head

        pre = head
        cur = head.next
        while True:
            if pre.val <= insertVal <= cur.val:
                break
                # newNode = Node(insertVal, cur)
                # pre.next = newNode
                # return head
            if cur.val < pre.val and (insertVal >= pre.val or insertVal <= cur.val):
                break
                # newNode = Node(insertVal, cur)
                # pre.next = newNode
                # return head

            pre = cur
            cur = cur.next
            if pre is head:
                break

        newNode = Node(insertVal, cur)
        pre.next = newNode
        return head
