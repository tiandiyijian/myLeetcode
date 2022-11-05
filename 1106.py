class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stk.append(c)
                continue
            t = f = 0
            while stk[-1] != '(':
                if stk.pop() == 't':
                    t += 1
                else:
                    f += 1
            stk.pop()
            op = stk.pop()
            if op == '!':
                stk.append('t' if t == 0 and f == 1 else 'f')
            elif op == '&':
                stk.append('t' if f == 0 else 'f')
            elif op == '|':
                stk.append('t' if t else 'f')
        return stk[-1] == 't'
