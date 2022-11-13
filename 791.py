class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: mp.get(x, -1)))
