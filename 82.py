# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        is_head_dup = False
        while True:
            is_head_dup = False
            while head.next is not None:
                if head.val == head.next.val:
                    is_head_dup = True
                    head = head.next
                else:
                    break
            if is_head_dup:
                head = head.next
            if head is None:
                return head
            if not is_head_dup:
                r_head = head
                break
        pre_head = head
        while head is not None and head.next is not None:
            if head.val != head.next.val:
                pre_head = head
                head = head.next
            else:
                while True:
                    if head.val == head.next.val:
                        head = head.next
                    if head.next is None:
                        break
                head = head.next
                pre_head.next = head
        return r_head
