from typing import Optional
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def move(node, step):
            for i in range(step):
                if node.next:
                    node = node.next
                else:
                    return node, i + 1
            return node, step + 1

        def reverse(node, reverse_len):
            pre = node
            cur = node.next
            for _ in range(reverse_len-1):
                next_cur = cur.next
                cur.next = pre
                pre = cur
                cur = next_cur
            return pre

        dummy = ListNode(next=head)
        cur = head
        pre = dummy
        cur_step = 1
        while cur:
            # print(cur.val)
            tmp_end, tmp_len = move(cur, cur_step-1)
            if tmp_len & 1 == 0:
                next_cur = tmp_end.next
                reverse_head = reverse(cur, tmp_len)
                pre.next = reverse_head
                cur.next = next_cur
                pre = cur
                cur = next_cur
            else:
                pre = tmp_end
                cur = pre.next
            cur_step += 1
        return dummy.next


def list2node(arr):
    dummy = ListNode()
    head = dummy
    for i in arr:
        head.next = ListNode(val=i)
        head = head.next
    return dummy.next


def printListNode(node):
    while node:
        print(node.val)
        node = node.next
        # time.sleep(1)


node = list2node([1, 1, 0, 6])

printListNode(Solution().reverseEvenLengthGroups(node))
