from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find_father(x):
            if father[x] != x:
                f = find_father(father[x])
                weight[x] *= weight[father[x]]
                father[x] = f
            return father[x]

        def merge(x, y, val):
            fx = find_father(x)
            fy = find_father(y)
            father[fx] = fy
            weight[fx] = val * weight[y] / weight[x]

        n = 0
        m = {}
        for [a, b] in equations:
            if a not in m:
                m[a] = n
                n += 1
            if b not in m:
                m[b] = n
                n += 1

        father = list(range(n))
        weight = [1.0] * n

        for (i, [a, b]) in enumerate(equations):
            idx_a, idx_b = m[a], m[b]
            merge(idx_a, idx_b, values[i])

        # print(m)
        # print(father)
        # print(weight)

        ans = []
        for [a, b] in queries:
            idx_a = m.get(a, None)
            idx_b = m.get(b, None)
            result = -1.0
            if idx_a is not None and idx_b is not None:
                fa = find_father(idx_a)
                fb = find_father(idx_b)
                if fa == fb:
                    result = weight[idx_a] / weight[idx_b]
            ans.append(result)

        return ans


if __name__ == "__main__":
    s = Solution()
    eqs = [["a", "b"], ["b", "c"]]
    vals = [2.0, 3.0]
    qs = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(s.calcEquation(eqs, vals, qs))
