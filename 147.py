# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        while head:
            node_to_insert = dummy
            while node_to_insert.next and node_to_insert.next.val < head.val:
                node_to_insert = node_to_insert.next
            tmp = node_to_insert.next
            node_to_insert.next = head
            head = head.next
            node_to_insert.next.next = tmp
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    print()
