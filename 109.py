# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next

        def build(low, high):
            if low > high:
                return None
            mid = (low + high) // 2

            left = build(low, mid - 1)

            nonlocal head
            node = TreeNode(head.val)
            head = head.next

            right = build(mid + 1, high)

            node.left = left
            node.right = right

            return node
        
        return build(0, length - 1)


if __name__ == "__main__":
    s = Solution()
    print()
