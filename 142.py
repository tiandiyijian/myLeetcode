# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        slow, fast = head, head
        while fast and fast.next:
            if fast is slow:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            slow = slow.next
            fast = fast.next.next
        return None
