# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        lastBack = ListNode(0)
        Rhead = head.next
        while True:
            p = head
            if p is None:
                break
            q = head.next
            if q is None:
                break
            head = q.next
            p.next = q.next
            q.next = p
            lastBack.next = q
            lastBack = p
        return Rhead
