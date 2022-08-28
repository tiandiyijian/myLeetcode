class Solution:
    def evaluate(self, expression: str) -> int:
        i = 0
        n = len(expression)
        values = []

        def findVal(token):
            for i in range(len(values) - 1, -1, -1):
                if token in values[i]:
                    return values[i][token]

        def helper(i):
            if i == n:
                return
            c = expression[i + 1]
            match c:
                case 'l':
                    cur_value = {}
                    values.append(cur_value)
                    i += 5
                    while True:
                        if expression[i] == '(':  # 一定是最后一个v
                            tmp = helper(i)
                            values.pop()
                            return tmp[0], tmp[1] + 1
                        j = i
                        while expression[j] != ' ' and expression[j] != ')':
                            j += 1
                        token = expression[i:j]

                        if expression[j] == ')':
                            if token.isdigit() or token[0] == '-':
                                values.pop()
                                return int(token), j
                            else:
                                ans = findVal(token), j
                                values.pop()
                                return ans

                        i = j + 1
                        if expression[i] == '(':
                            v, nxt_i = helper(i)
                            i = nxt_i + 2
                        else:
                            j = i
                            while expression[j] != ' ':
                                j += 1
                            tokenV = expression[i:j]
                            v = (
                                int(tokenV)
                                if (tokenV.isdigit() or tokenV[0] == '-')
                                else findVal(tokenV)
                            )
                            i = j + 1

                        cur_value[token] = v
                case 'a' | 'm':
                    i += 5 if c == 'a' else 6
                    if expression[i] == '(':
                        v1, nxt_i = helper(i)
                        i = nxt_i + 2
                    else:
                        j = i
                        while expression[j] != ' ':
                            j += 1
                        token = expression[i:j]
                        v1 = (
                            int(token)
                            if (token.isdigit() or token[0] == '-')
                            else findVal(token)
                        )
                        i = j + 1

                    if expression[i] == '(':
                        v2, nxt_i = helper(i)
                        i = nxt_i + 1
                    else:
                        j = i
                        while expression[j] != ')':
                            j += 1
                        token = expression[i:j]
                        v2 = (
                            int(token)
                            if (token.isdigit() or token[0] == '-')
                            else findVal(token)
                        )
                        i = j
                    return (v1 + v2, i) if c == 'a' else (v1 * v2, i)

        return helper(0)[0]


e = "(let x (add 2 3) y (mult 3 (add 2 2)) z (let x) (add 1 2))"
e = "(let z (let 2) (add 2 3))"
e = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
e = "(let x 2 (add (let x 3 (let x 4 x)) x))"
e = "(let x 2 (mult (let x 3 y 4 (add x y)) x))"
e = "(let x 7 -12)"
e = "(let x -2 y x y)"
e = "(let x0 4 x1 -2 x2 3 x3 -5 x4 -3 x5 -1 x6 3 x7 -2 x8 4 x9 -5 (mult x2 (mult (let x0 -3 x4 -2 x8 4 (mult (let x0 -2 x6 4 (add x5 x2)) x3)) (mult (mult -7 (mult -9 (let x0 -2 x7 3 (add -10 x0)))) x6))))"
print(Solution().evaluate(e))
