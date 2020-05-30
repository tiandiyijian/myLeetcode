from typing import List


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def sToArray(S):    
            i = 0
            tmp = []
            while i < len(S):
                start = i
                while i+1 < len(S) and S[i] == S[i+1]:
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
                            
            



if __name__ == "__main__":
    s = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(s.expressiveWords(S, words))