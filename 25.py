# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(node):
            head = node
            nodes_num = 1
            while(head.next):
                head = head.next
                nodes_num += 1
            pre_head = node
            if nodes_num < k:
                return head, pre_head, None
            next_node2 = node.next
            for _ in range(k-2):
                next_node = next_node2
                next_node2 = next_node.next
                next_node.next = node
                node = next_node
            next_head = next_node2.next
            next_node2.next = node
            return pre_head, next_node2, next_head

        if k == 1:
            return head
        phead = pre_head = ListNode(-1)
        # pre_head.next = head
        while head:
            end, head, next_head = reverse(head)
            pre_head.next = head
            pre_head = end
            pre_head.next = None
            # print(end, head, next_head)
            head = next_head
        return phead.next


if __name__ == "__main__":
    s = Solution()
    print()
    #第二次写了，希望再碰见能写出更简洁的
