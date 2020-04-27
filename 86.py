# Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        littleHead = ListNode(-1)
        bigHead = ListNode(-1)
        L, B = littleHead, bigHead
        #littleHead.next = head
        while head is not None:
            if head.val < x:
                littleHead.next = head
                littleHead = head
            else:
                tem = ListNode(head.val)
                bigHead.next = tem
                bigHead = bigHead.next
            head = head.next
        littleHead.next = B.next
        return L.next