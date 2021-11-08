class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        m1, m2 = collections.defaultdict(int), collections.defaultdict(int)
        a = b = 0
        for s, g in zip(secret, guess):
            if s == g:
                a += 1
            else:
                m1[s] += 1
                m2[g] += 1
        for key in m2:
            b += min(m1[key], m2[key])
        return f'{a}A{b}B'