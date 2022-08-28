from collections import defaultdict, deque
from typing import List


class Solution:

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        if start == end:
            return 0

        graph = defaultdict(list)
        if start not in bank:
            bank.append(start)
        n = len(bank)
        for i in range(n):
            for j in range(i + 1, n):
                if validate(bank[i], bank[j]):
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])

        q = deque([(start, 0)])
        visit = {start}
        while q:
            node, d = q.popleft()
            for nei in graph[node]:
                if nei == end:
                    return d + 1
                if nei not in visit:
                    q.append((nei, d + 1))
                    visit.add(nei)
        return -1


def validate(a: str, b: str) -> bool:
    flag = False
    for x, y in zip(a, b):
        if x != y:
            if flag:
                return False
            flag = True
    return True
