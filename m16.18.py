import collections


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        lenv = len(value)
        if len(pattern) > 0 and pattern[0] == 'b':
            pattern = ''.join(map(lambda x: 'a' if x == 'b' else 'b', pattern))
        counter = collections.Counter(pattern)
        if not value:
            return not pattern or bool(counter['a'] ^ counter['b'])
        if pattern == 'a' or pattern == 'b' or pattern == 'ab' or pattern == 'ba':
            return True
        if counter['a'] == 0:
            lenb = lenv / counter['b']
            if lenb % 1 != 0:
                return False
            b = value[:int(lenb)]
            return b * counter['b'] == value
        if counter['b'] == 0:
            lena = lenv / counter['a']
            if lena % 1 != 0:
                return False
            a = value[:int(lena)]
            return a * counter['a'] == value
        # print(pattern)
        first_b = pattern.index('b')
        for i in range(lenv // counter['a'] + 1):
            # print(i)
            a = value[:i]
            lenb = (lenv - i * counter['a']) / counter['b']
            if lenb > 1 and lenb % 1 != 0:
                # print(f'jump{lenb}')
                continue
            lenb = int(lenb)
            b = value[i*first_b: i*first_b + lenb]
            tmp = ''
            for c in pattern:
                if c == 'a':
                    tmp += a
                else:
                    tmp += b
            if tmp == value:
                return True
        # print(lenb, a, b, tmp, value, sep='\n')
        # print(a == value)
        # print(b)
        return False


if __name__ == "__main__":
    s = Solution()
    p = "bbbbbbbbabbbbbbbbbbbabbbbbbba"
    v = "zezezezezezezezezkxzezezezezezezezezezezezkxzezezezezezezezkx"
    print(len(v))
    print(s.patternMatching(p, v))
