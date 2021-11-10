class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        return [s for s in words if (all(l in a for l in s.lower()) or all(l in b for l in s.lower()) or all(l in c for l in s.lower()))]
