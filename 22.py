from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # start = {'()'}
        # if n == 1:
        #     return start
        # for _ in range(n-1):
        #     tmp = set()
        #     for item in start:
        #         tmp.add(item + '()')
        #         tmp.add('()' + item)
        #         tmp.add('(' + item + ')')
        #     start = tmp
        # return list(start)
        def generate(cur, open, close):
            if open == close == 0:
                ans.append(cur[:])
            if open > 0:
                cur += '('
                generate(cur, open-1, close)
                cur = cur[:-1]
            if close > open:
                cur += ')'
                generate(cur, open, close-1)
                cur = cur[:-1]
        ans = []
        generate('', n, n)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(4))
