class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        mp = {}
        pre_letters = set()
        for i, letter in enumerate(pattern):
            if letter in mp:
                if mp[letter] != words[i]:
                    return False
            elif words[i] in pre_letters:
                return False
            else:
                mp[letter] = words[i]
                pre_letters.add(words[i])
        return True


if __name__ == "__main__":
    s = Solution()
    print()