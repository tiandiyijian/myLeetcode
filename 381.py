from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list = []
        self._val_idx = defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self._val_idx:
            ans = False
        else:
            ans = True
        self._list.append(val)
        self._val_idx[val].append(len(self._list) - 1)
        return ans

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        indices = self._val_idx[val]
        if not indices:
            return False
        else:
            if val == self._list[-1]:
                self._list.pop()
                self._val_idx[val].remove(len(self._list))
                return True
            idx = indices.pop()
            last_val = self._list[-1]
            self._list[idx], self._list[-1] = self._list[-1], self._list[idx]
            last_val_indices = self._val_idx[last_val]
            last_val_indices[last_val_indices.index(len(self._list) - 1)] = idx
            self._list.pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self._list[random.randint(0, len(self._list) - 1)]


if __name__ == "__main__":
    # Your RandomizedCollection object will be instantiated and called as such:
    obj = RandomizedCollection()
    param_1 = obj.insert(1)
    param_2 = obj.remove(2)
    param_3 = obj.getRandom()
    import IPython; IPython.embed()
