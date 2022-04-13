from random import randint


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.indices = {}
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        if self.len == len(self.list):
            self.list.append(val)
        else:
            self.list[self.len] = val
        self.indices[val] = self.len
        self.len += 1 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        idx = self.indices[val]
        self.list[idx] = self.list[self.len-1]
        self.len -= 1
        self.indices[self.list[idx]] = idx
        del self.indices[val]
        # print(self.indices, self.list, self.len, val)
        return True

    def getRandom(self) -> int:
        return self.list[randint(0, self.len-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()