import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # m, n = len(ransomNote), len(magazine)
        # if m > n:
        #     return False
        # cnt = [0] * 26
        # for a, b in zip_longest(ransomNote, magazine):
        #     if a is not None:
        #         cnt[ord(a)-ord('a')] -= 1
        #     cnt[ord(b)-ord('a')] += 1
        # return all(x >= 0 for x in cnt)

        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
