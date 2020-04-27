# Definition for singly-linked list.
import collections

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = collections.deque(), collections.deque()
        node1, node2 = l1, l2
        while node1:
            stack1.append(node1.val)
            node1 = node1.next
        while node2:
            stack2.append(node2.val)
            node2 = node2.next
        ans = collections.deque()
        carry = 0
        # while stack1 and stack2:
        #     sum = stack1.pop() + stack2.pop() + carry
        #     carry = sum // 10
        #     ans.appendleft(sum % 10)
        # while stack1:
        #     sum = stack1.pop() + carry
        #     carry = sum // 10
        #     ans.appendleft(sum % 10)
        # while stack2:
        #     sum = stack2.pop() + carry
        #     carry = sum // 10
        #     ans.appendleft(sum % 10)
        # if carry == 1:
        #     ans.appendleft(1)
        while stack1 or stack2 or carry != 0:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            sum = num1 + num2 + carry
            carry = sum // 10
            ans.appendleft(sum % 10)
        l = ListNode(-1)
        node = l
        while ans:
            node.next = ListNode(ans.popleft())
            node = node.next
        return l.next

if __name__ == "__main__":
    s = Solution()
    print()