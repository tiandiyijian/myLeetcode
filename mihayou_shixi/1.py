#coding=utf-8
# 直接判断合法的括号有多少
import sys
from collections import deque
s = sys.stdin.readline()
stack = deque([])
ans = 0
left = {'(', '{', '['}
for c in s:
    if c == '}' and stack and stack[-1] == '{':
        ans += 3
        stack.pop()
    elif c == ']' and stack and stack[-1] == '[':
        ans += 2
        stack.pop()
    elif c == ')' and stack and stack[-1] == '(':
        ans += 1
        stack.pop()
    else:
        stack.append(c)
    # print(stack, ans)
print(ans)