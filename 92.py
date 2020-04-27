class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        thead = head
        i = 1
        front = head
        while i < m:
            if i == m - 1:
                front = head
            head = head.next
            i += 1
        reverse_end = head
        prev = head
        head = head.next
        while i < n:
            tem = head.next
            head.next = prev
            prev = head
            head = tem
            i += 1
        front.next = prev
        reverse_end.next = head
        if m == 1:
            return prev
        return thead
