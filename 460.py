import collections


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex

    def __str__(self):
        return f'key:{self.key} val:{self.val}'

def create_linked_list():
    head = Node(0, 0)
    tail = Node(100, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):
        if node.pre:
            print('delete')
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                print(self.freqMap.keys())
                self.freqMap.pop(node.freq)
                print(self.freqMap.keys())
                print(f'pop freq{node.freq}')
        return node.key

    def increase(self, node):
        self.delete(node)
        node.freq += 1
        self.freqMap[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            # head, tail = self.freqMap[node.freq - 1]
            # if head.nex is tail:
            if node.freq - 1 not in self.freqMap:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)
                self.keyMap.pop(deleted)
            self.increase(node)

if __name__ == "__main__":
# Your LFUCache object will be instantiated and called as such:
    obj = LFUCache(2)
    param_1 = obj.get(1)
    obj.put(2, 2)
    import IPython; IPython.embed()
