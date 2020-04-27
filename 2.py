# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(-1)
        node = head
        while(l1 and l2):
            sum = l1.val + l2.val + carry
            if (sum >= 10):
                sum -= 10
                carry = 1
            else: carry = 0
            node.next = ListNode(sum)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            if (sum >= 10):
                sum -= 10
                carry = 1
            else: carry = 0
            node.next = ListNode(sum)
            node = node.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            if (sum >= 10):
                sum -= 10
                carry = 1
            else: carry = 0
            node.next = ListNode(sum)
            node = node.next
            l2 = l2.next
        if carry:
            node.next = ListNode(1)
        return head.next