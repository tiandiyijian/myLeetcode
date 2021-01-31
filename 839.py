from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        def judge(i, j):
            count = 0
            for a, b in zip(strs[i], strs[j]):
                if a != b:
                    count += 1
            return count <= 2

        f = list(range(n))
        rank = [1] * n
        count = n

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy:
                return
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            f[fy] = fx
            rank[fx] += rank[fy]
            nonlocal count
            count -= 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if judge(i, j):
                    union(i, j)
        return count


if __name__ == "__main__":
    s = Solution()
    print()
