class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 刚开始并没有想到怎么解决跳过的字母里有'#'的问题
        # 看过答案之后发现别一下子跳过，一步一步地跳就行了，中间遇到'#'只需要增加skip就好了
        i, j = len(S) - 1, len(T) - 1
        skip_S = skip_T = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skip_S += 1
                    i -= 1
                elif skip_S > 0:
                    i -= 1
                    skip_S -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skip_T += 1
                    j -= 1
                elif skip_T > 0:
                    j -= 1
                    skip_T -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("bxj##tw", "bxo#j##tw"))
