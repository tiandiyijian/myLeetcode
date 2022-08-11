from itertools import zip_longest


class Solution:
    def reformat(self, s: str) -> str:
        # 也可以统计过数量之后边遍历边填充
        digit, letter = [], []

        for c in s:
            if c.isdigit():
                digit.append(c)
            else:
                letter.append(c)

        if len(digit) >= len(letter):
            a, b = digit, letter
        else:
            a, b = letter, digit

        if len(a) - len(b) > 1:
            return ''

        return ''.join(x[0] + x[1] for x in zip_longest(a, b, fillvalue=''))
