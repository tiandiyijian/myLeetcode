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

    def partition2(self, head: ListNode, x: int) -> ListNode:
        pre = dummy_a = ListNode(-1)
        post = dummy_b = ListNode(-1)

        while head:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                post.next = head
                post = post.next
            head = head.next
        
        post.next = None
        pre.next = dummy_b.next

        return dummy_a.next