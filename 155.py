class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            if x < self.stack[-1][1]:
                self.stack.append((x, x))
            else:
                self.stack.append((x, self.stack[-1][1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3, param_4)
