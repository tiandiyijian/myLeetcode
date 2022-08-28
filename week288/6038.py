from sys import prefix


class Solution:
    def minimizeResult(self, expression: str) -> str:
        n = len(expression)
        mid = expression.index('+')
        min_exp = float('inf')
        l_size = r_size = 0
        for l in range(1, mid+1):
            l_inner = int(expression[mid-l:mid])
            prefix = int(expression[:mid-l]) if l < mid else 1
            for r in range(1, n-mid):
                r_inner = int(expression[mid+1:mid+1+r])
                postfix = int(expression[mid+1+r:]) if mid + 1 + r < n else 1
                cur = prefix * (l_inner + r_inner) * postfix
                if cur < min_exp:
                    min_exp = cur
                    l_size = l
                    r_size = r
        return expression[:mid-l_size] + "(" + expression[mid-l_size:mid+1+r_size] + ")" + expression[mid+1+r_size:]

print(Solution().minimizeResult('999+999'))

