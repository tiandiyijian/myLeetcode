# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(a, b):
            if not (a and b):
                return a if a else b
            dummy = ListNode(float('-inf'))
            current = dummy
            while a and b:
                if a.val < b.val:
                    current.next = a
                    a = a.next
                else:
                    current.next = b
                    b = b.next
                current = current.next
            current.next = a or b
            return dummy.next

        def split(node):
            if not node or not node.next:
                return node
            a = b = node
            while b.next and b.next.next:
                a = a.next
                b = b.next.next
            mid = a.next
            a.next = None
            return mid
        if not head or not head.next:
            return head
        mid = split(head)
        pre = self.sortList(head)
        post = self.sortList(mid)
        return merge(pre, post)


if __name__ == "__main__":
    s = Solution()
    print()
