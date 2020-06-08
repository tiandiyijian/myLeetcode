from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        p = list(range(26))

        def find(x):
            l = 1
            while x != p[x]:
                x = p[x]
                l += 1
            return x, l

        def union(x, y):
            px, lx = find(x)
            py, ly = find(y)
            if lx < ly:
                p[px] = py
            else:
                p[py] = px

        for eq in equations:
            if eq[1] == '=':
                x, y = ord(eq[0]) - 97, ord(eq[-1]) - 97
                # if find(x) == find(y):
                #     continue
                # else:
                union(x, y)

        for eq in equations:
            if eq[1] == '!':
                x, y = ord(eq[0]) - 97, ord(eq[-1]) - 97
                if find(x)[0] == find(y)[0]:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    eq = ["a==b","b!=c","c==a"]
    print(s.equationsPossible(eq))
