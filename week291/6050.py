from collections import defaultdict


class Solution:

    def appealSum(self, s: str) -> int:
        n = len(s)
        mp = defaultdict(list)
        for i, c in enumerate(s):
            mp[c].append(i)

        ans = 0
        for indices in mp.values():
            ans += (indices[0] + 1) * (n - indices[0])
            for i in range(1, len(indices)):
                pre = indices[i] - indices[i - 1]
                post = n - indices[i]
                ans += pre * post

        return ans


def validate(s: str):
    n = len(s)
    ans = 0
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            sub = s[i:i + l]
            ans += len(set(sub))
            # print(sub, ans)
    return ans


s = "ktttt"
print(Solution().appealSum(s))
print(validate(s))