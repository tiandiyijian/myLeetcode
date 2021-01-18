from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self):
        """
        docstring
        """
        self.f = {}
        self.rank = {}

    def find(self, a):
        if a not in self.f:
            self.f[a] = a
            self.rank[a] = 1
        elif self.f[a] != a:
            self.f[a] = self.find(self.f[a])
        return self.f[a]

    def union(self, a, b):
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return
        if self.rank[a] > self.rank[b]:
            fa, fb = fb, fa
        self.f[fa] = fb
        self.rank[fb] += self.rank[fa]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        UF = UnionFind()
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                UF.union((account[i], name), (account[1], name))

        mp = defaultdict(list)
        for (mail, name) in UF.f.keys():
            father = UF.find((mail, name))
            mp[father].append(mail)
        ans = [[name] + sorted(mails) for (_, name), mails in mp.items()]
        return ans


if __name__ == "__main__":
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(s.accountsMerge(accounts))
