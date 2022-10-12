from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        while head:
            if head.val not in nums:
                head = head.next
            else:
                tmp = head.next
                while tmp and tmp.val in nums:
                    tmp = tmp.next
                ans += 1
                head = tmp

        return ans
