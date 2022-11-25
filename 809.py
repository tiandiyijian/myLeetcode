from typing import List


class Solution_1:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def sToArray(S):
            i = 0
            tmp = []
            while i < len(S):
                start = i
                while i + 1 < len(S) and S[i] == S[i + 1]:
                    i += 1
                count = i - start + 1
                if count >= 3:
                    tmp.append((S[i], -count))
                else:
                    tmp.append((S[i], count))
                i += 1
            return tmp

        S_array = sToArray(S)
        # print(S_array)
        ans = 0
        for word in words:
            w_array = sToArray(word)
            if len(w_array) != len(S_array):
                continue
            else:
                flag = True
                for i in range(len(S_array)):
                    if S_array[i][0] != w_array[i][0]:
                        flag = False
                        break
                    else:
                        if S_array[i][1] > 0:
                            if w_array[i][1] != S_array[i][1]:
                                flag = False
                                break
                        else:
                            # print(w_array[i])
                            if abs(w_array[i][1]) > -S_array[i][1]:
                                flag = False
                                break
                if flag:
                    ans += 1
        return ans


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        groups = []
        pre_idx = 0
        pre_chr = s[0]
        for i, c in enumerate(s):
            if c != pre_chr:
                groups.append((pre_chr, i - pre_idx))
                pre_idx = i
                pre_chr = c
        groups.append((s[-1], len(s) - pre_idx))
        # print(groups)

        ans = 0
        for w in words:
            g_idx = 0
            pre_idx = 0
            pre_chr = w[0]
            for i, c in enumerate(w):
                if c != pre_chr:
                    gc, gl = groups[g_idx]
                    l = i - pre_idx
                    # print(i,c,l, gc, gl)
                    if pre_chr != gc or l > gl or (l < gl and gl < 3):
                        break
                    pre_idx = i
                    pre_chr = c
                    g_idx += 1
                    if g_idx == len(groups):
                        break
            else:
                gc, gl = groups[g_idx]
                l = len(w) - pre_idx
                if pre_chr != gc or l > gl or (l < gl and gl < 3):
                    continue
                g_idx += 1
                if g_idx == len(groups):
                    ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(s.expressiveWords(S, words))
