from collections import deque

OPEN = 0
CLOSE = 1


class Solution:

    def isValid(self, code: str) -> bool:
        i = 0
        n = len(code)
        if n == 0 or code[0] != '<' or code[:9] == '<![CDATA[':
            return False
        s = deque()
        while i < n:
            if code[i] == '<':
                if i + 1 < n:
                    if code[i + 1] == '/':
                        j = i + 2
                        while j < n and code[j] != '>':
                            if not code[j].isupper():
                                return False
                            j += 1
                        if not s or s[-1] != (OPEN, code[i + 2:j]):
                            return False
                        else:
                            s.pop()
                        i = j + 1
                        if i < n and not s:
                            return False
                        continue
                    elif code[i:i + 9] == '<![CDATA[':
                        j = i + 9
                        while j + 3 <= n and (code[j] != ']'
                                              or code[j:j + 3] != ']]>'):
                            j += 1
                        if j + 3 > n:
                            return False
                        i = j + 3
                        continue
                    else:
                        j = i + 1
                        while j < n and code[j] != '>':
                            if not code[j].isupper():
                                return False
                            j += 1
                        if j == i + 1 or j - i - 1 > 9:
                            return False
                        s.append((OPEN, code[i + 1:j]))
                        i = j + 1
                        continue
                else:
                    return False
            else:
                i += 1

        return not s


code = '<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>'
code = '<DIV>This is the first line <![CDATA[<div>]]></DIV>'
code = '<A>  <B> </A>   </B>'
code = '<DIV>  div tag is not closed  <DIV>'
code = '<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>'
print(Solution().isValid(code))