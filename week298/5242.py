class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ''
        for i in range(ord('A'), ord('A') + 26):
            if chr(i) in s and chr(i).lower() in s:
                ans = chr(i)

        return ans
