from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordDict = set(wordDict)
        @lru_cache()
        def dfs(start):
            if start >= len(s):
                return ['']
            ans = []
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in wordDict:
                    tmp = dfs(i)
                    for tmp_s in tmp:
                        if tmp_s:
                            ans.append(s[start:i] + ' ' + tmp_s)
                        else:
                            ans.append(s[start:i])
            return ans

        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    print()
