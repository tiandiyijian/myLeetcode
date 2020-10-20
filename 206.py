# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head or not head.next: return head
        # a, b = None, head
        # while b:
        #     tmp = b.next
        #     b.next = a
        #     a = b
        #     b = tmp
        # return a
        if not head or not head.next: return head
        a, b = None, head
        def reverse(a, b):
            if not b: return a
            tmp = b.next
            b.next = a
            # a, b = b, tmp
            return reverse(b, tmp)
        return reverse(a, b)


    def reverseList2(self, head: ListNode) -> ListNode:
        a, b = None, head
        while b:
            tmp = b.next
            b.next = a
            a = b
            b = tmp
        return a
            

def change_node(node):
    node = node.next
    return node

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    print(id(a), id(b), id(change_node(a)), id(a), a.val)

