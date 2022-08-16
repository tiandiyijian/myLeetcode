from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * (n+1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value

        if idKey == self.ptr:
            ans = []
            while self.ptr < len(self.values) and self.values[self.ptr] is not None:
                ans.append(self.values[self.ptr])
                self.ptr += 1
            return ans
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
