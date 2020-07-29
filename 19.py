# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = ListNode(-1)
        tmp.next = head
        a = b = tmp
        for _ in range(n):
            a = a.next
        while a.next:
            a = a.next
            b = b.next
        b.next = b.next.next
        return tmp.next


if __name__ == "__main__":
    s = Solution()
    print()
