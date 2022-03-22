class Solution:

    def winnerOfGame(self, colors: str) -> bool:
        a_cnt = 0
        b_cnt = 0
        i = 0
        n = len(colors)
        while i < n:
            cnt = 1
            j = i + 1
            while j < n:
                if colors[j] != colors[i]:
                    break
                cnt += 1
                j += 1
            if colors[i] == 'A':
                a_cnt += (cnt - 2) if cnt >= 3 else 0
            else:
                b_cnt += (cnt - 2) if cnt >= 3 else 0
            i = max(i + 1, j)
        return a_cnt > b_cnt