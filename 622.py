class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * (k)
        self.front = 0
        self.rear = 0
        self.size = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.size >= self.cap:
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size > 0:
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        if self.size > 0:
            return self.q[self.front]
        return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.q[(self.rear - 1) % self.cap]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
