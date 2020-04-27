# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeList(a: ListNode, b: ListNode):
            dummy = ListNode(-1)
            rhead = dummy
            while a and b:
                if a.val < b.val:
                    rhead.next = a
                    a = a.next
                else:
                    rhead.next = b
                    b = b.next
                rhead = rhead.next
            rhead.next = a or b
            return dummy.next
        if not lists: return None
        n = len(lists)
        while (n > 1):
            halfLen = int((n + 1) / 2)
            # print(halfLen)
            for i in range(int(n/2)):
                # print(i, i + halfLen)
                lists[i] = mergeList(lists[i], lists[i + halfLen])
            n = halfLen
        return lists[0]
    