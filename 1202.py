import collections
from typing import List


class UnionFind:
    def __init__(self, n):
        """
        Union-find
        """
        self.f = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.f[i] == i:
            return i
        self.f[i] = self.find(self.f[i])
        return self.f[i]

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)

        if fa == fb:
            return
        if self.rank[fa] > self.rank[fb]:
            fa, fb = fb, fa
        self.f[fa] = fb
        self.rank[fb] += self.rank[fa]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        UF = UnionFind(n)

        for [a, b] in pairs:
            UF.union(a, b)

        mp = collections.defaultdict(list)
        for i in range(n):
            mp[UF.find(i)].append(s[i])

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = ''
        for i in range(n):
            ans += mp[UF.find(i)].pop()
        return ans


if __name__ == "__main__":
    s = Solution()
    strs = "dcab"
    pairs = [[0, 3], [1, 2]]
    print(s.smallestStringWithSwaps(strs, pairs))
