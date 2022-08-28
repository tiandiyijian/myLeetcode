from sortedcontainers import SortedSet


class SmallestInfiniteSet:
    def __init__(self):
        self.set = SortedSet(range(1, 1001))

    def popSmallest(self) -> int:
        return self.set.pop(0)

    def addBack(self, num: int) -> None:
        self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
