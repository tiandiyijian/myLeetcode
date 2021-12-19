from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def judge(word: str):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        for s in words:
            if judge(s):
                return s
        return ""
