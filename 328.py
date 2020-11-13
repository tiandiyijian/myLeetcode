# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        a, b = head, head.next
        ta, tb = a, b

        while b and b.next:
            a.next = b.next
            a = a.next

            b.next = a.next
            b = b.next
        a.next = tb
        return ta


if __name__ == "__main__":
    s = Solution()
    print()
