from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs: return ""
        # max_len = len(strs[0])
        # for i in range(1, len(strs)):
        #     max_len = min(max_len, len(strs[i]))
        #     for j in range(max_len):
        #         if strs[i][j] != strs[0][j]:
        #             max_len = j
        #             break
        # # print(max_len)
        # return strs[0][0:max_len]

        # if not strs or not strs[0]: return ""
        # max_pre_length = len(min(strs, key=len))
        # # print(max_pre_length)
        # for i in range(max_pre_length):
        #     for str in strs[1:]:
        #         if str[i] != strs[0][i]:
        #             return str[:i]
        # return strs[0][:max_pre_length]

        if not strs: return ""
        length = 0
        for i in zip(*strs):
            if len(set(i)) == 1:
                length += 1
            else:
                return strs[0][:length]
        return strs[0][:length]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    # strs = ["flower","flow","flight"]
    # strs = [1, 2, 3]
    # for i in zip(*strs):
    #     print(i)