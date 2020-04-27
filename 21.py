# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b = l1, l2
        head = node = ListNode(-1)
#             node = a if a.val < b.val else b
        while a and b:
            if a.val < b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next
        # node.next = b if a is None else a
        node.next = a or b
        return head.next
            # dummy = ListNode(-1)
            # head = dummy
            # while a or b:
            #     if a and (not b or a.val <= b.val):
            #         print(not b)
            #         head.next = a
            #         a = a.next
            #     elif b and (not a or b.val < a.val):
            #         print(not a)
            #         head.next = b
            #         b = b.next
            #     print(head.val)
            #     head = head.next
            # return dummy.next