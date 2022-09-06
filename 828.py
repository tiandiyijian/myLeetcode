import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 单独考虑每一个字符对结果的贡献
        # 贡献就是它所在的不包含另一个相同字母的子字符串的个数
        # 那就是左边个数乘右边个数
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res
