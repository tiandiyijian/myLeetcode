# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        s = set()
        pre = None
        node = head
        while node:
            if node.val in s:
                pre.next = node.next
            else:
                pre = node
                s.add(node.val)
            node = pre.next
        return head



if __name__ == "__main__":
    s = Solution()
    print()