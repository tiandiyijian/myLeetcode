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

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            tmp_sum = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            head.next = ListNode(tmp_sum)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head = head.next
        return dummy.next