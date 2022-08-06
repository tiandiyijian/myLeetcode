from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        words.sort(key=lambda x: -len(x))

        for i in range(1, len(words)):
            for j in range(i):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans
