# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head: return head
        
        length = 0
        rear = head
        while rear.next:
            length += 1
            rear = rear.next
        length += 1
        
        k = k % length
        if k == 0: return head

        right_head = head
        for i in range(length - k - 1):
            right_head = right_head.next
        tmp = right_head
        right_head = right_head.next
        tmp.next = None
        rear.next = head
        head = right_head
        return head
        
        