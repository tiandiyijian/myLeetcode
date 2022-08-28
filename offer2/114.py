from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def alienOrder1(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = defaultdict(int)
        for c in words[0]:
            inDeg[c] = 0
        for a, b in pairwise(words):
            for p, q in zip(a, b):
                for c in b:
                    inDeg.setdefault(c, 0)
                if p != q:
                    # 这里可能会出现重复添加的问题, 但是也没有问题, 添加了多少次后面广搜的时候就会减多少次
                    # 也可以使用set来避免这个问题
                    g[p].append(q)
                    inDeg[q] += 1
                    break
            else:
                if len(a) > len(b):
                    return ''

        ans = list(c for c, ind in inDeg.items() if ind == 0)
        for c in ans:
            for nxt in g[c]:
                inDeg[nxt] -= 1
                if inDeg[nxt] == 0:
                    ans.append(nxt)
                    # Python可以迭代数组的同时插入
                    # 直接就可以广度优先搜索了

        return ''.join(ans) if len(ans) == len(inDeg) else ''

    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(set)
        inDeg = defaultdict(int)
        for c in words[0]:
            inDeg[c] = 0
        for a, b in pairwise(words):
            for p, q in zip(a, b):
                for c in b:
                    inDeg.setdefault(c, 0)
                if p != q:
                    if p in g[q]:
                        return ''
                    if q not in g[p]:
                        g[p].add(q)
                        inDeg[q] += 1
                    break
            else:
                if len(a) > len(b):
                    return ''

        ans = list(c for c, ind in inDeg.items() if ind == 0)
        for c in ans:
            for nxt in g[c]:
                inDeg[nxt] -= 1
                if inDeg[nxt] == 0:
                    ans.append(nxt)
                    # Python可以迭代数组的同时插入
                    # 直接就可以广度优先搜索了

        return ''.join(ans) if len(ans) == len(inDeg) else ''


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(Solution().alienOrder(words))
