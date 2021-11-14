_val = '_val'


class MapSum:

    def __init__(self):
        self.root = {}
        self.mp = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.mp:
            delta -= self.mp[key]
        self.mp[key] = val
        root = self.root
        for c in key:
            root = root.setdefault(c, {})
            if _val in root:
                root[_val] += delta
            else:
                root[_val] = delta

    def sum(self, prefix: str) -> int:
        root = self.root
        ans = 0
        for c in prefix:
            if c not in root:
                return 0
            root = root[c]
        return root[_val]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
