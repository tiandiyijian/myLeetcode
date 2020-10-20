# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        mid = self.middleNode(head)
        reverse_right = self.reverseList(mid)
        l, r = head, reverse_right
        while True:
            next_l, next_r = l.next, r.next
            if next_l is r:
                break
            if next_l is next_r:
                l.next = r
                break
            l.next = r
            r.next = next_l
            l, r = next_l, next_r
        return head

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        a, b = None, head
        while b:
            tmp = b.next
            b.next = a
            a = b
            b = tmp
        return a


if __name__ == "__main__":
    s = Solution()
    print()
