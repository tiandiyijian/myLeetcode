from collections import deque


class CQueue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def appendTail(self, value: int) -> None:
        self.q1.append(value)

    def deleteHead(self) -> int:
        if self.q2:
            return self.q2.pop()
        else:
            while self.q1:
                self.q2.append(self.q1.pop())
            if self.q2:
                return self.q2.pop()
            else:
                return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()