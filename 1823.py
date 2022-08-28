class Node:

    def __init__(self, val=-1, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt


class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        if k == 1:
            return n

        head = Node(1)
        pre = head
        for i in range(2, n + 1):
            cur = Node(i)
            cur.pre = pre
            pre.nxt = cur
            pre = cur
        cur.nxt = head
        head.pre = cur

        # start = head
        # for _ in range(10):
        #     print(start.val)
        #     start = start.nxt

        cnt = n
        p = head
        while cnt > 1:
            for _ in range(k - 1):
                p = p.nxt
            p.pre.nxt = p.nxt
            p.nxt.pre = p.pre
            p = p.nxt
            cnt -= 1

        return p.val
