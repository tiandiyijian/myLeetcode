class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        if n < 6:
            return 0
        mp = defaultdict(set)
        ans = 0
        for i in range(n>>1):
            mp[rings[i*2 +1]].add(rings[i*2])

        for v in mp.values():
            if len(v) == 3:
                ans += 1
        return ans