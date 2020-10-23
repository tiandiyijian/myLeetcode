# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        mid = self.midOfList(head)
        rhead = self.reverseList(mid.next)
        a, b = head, rhead
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        mid.next = self.reverseList(rhead)
        return True

    def reverseList(self, head):
        a, b = None, head
        while b:
            tmp = b.next
            b.next = a
            a = b
            b = tmp
        return a

    def midOfList(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    s = Solution()
    print()
