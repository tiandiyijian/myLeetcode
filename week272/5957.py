from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = s[:spaces[0]] + " "
        for i in range(1, len(spaces)):
            ans += s[spaces[i-1]:spaces[i]] + " "
        ans += s[spaces[-1]:]
        return ans


s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
print(Solution().addSpaces(s, spaces))
