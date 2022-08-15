class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.cap = k
        self.front = self.rear = 0
        self.d = [0] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.d[0] = value
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.cap
            self.d[self.front] = value

        self.size += 1
        # print(self.d, self.front, self.rear)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.d[0] = value
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.cap
            self.d[self.rear] = value

        self.size += 1
        # print(self.d, self.front, self.rear)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.cap
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.d[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.d[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
