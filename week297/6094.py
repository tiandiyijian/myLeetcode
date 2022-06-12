from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        st = set(ideas)

        cnt = [[0] * 26 for _ in range(26)]
        flag = [[0] * 26 for _ in range(n)]
        for i in range(n):
            old = ord(ideas[i][0]) - ord('a')
            for j in range(26):
                new_str = chr(ord('a') + j) + ideas[i][1:]
                if new_str not in st:
                    flag[i][j] = True
                    cnt[old][j] += 1

        ans = 0
        for i in range(n):
            for j in range(26):
                if flag[i][j]:
                    ans += cnt[j][ord(ideas[i][0]) - ord('a')]

        return ans
