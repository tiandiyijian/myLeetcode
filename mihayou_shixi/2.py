#coding=utf-8
# 贪心
import sys
s = sys.stdin.readline().strip()
n = len(s)
ans = 0
l = 0
r = 0
while l < n:
    if s[l] == '0':
        l += 1
    else:
        r = l
        while r < n and s[r] == '1':
            r += 1
        size = r - l
        if size & 1 == 1:
            ans += 1
        l = r
    # print(l)
print(ans)
