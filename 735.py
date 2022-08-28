from collections import deque
from typing import List


class Solution:
    def asteroidCollision1(self, asteroids: List[int]) -> List[int]:
        # 错误思路
        ans = []
        n = len(asteroids)

        i = 0
        while i < n:
            if asteroids[i] < 0:
                ans.append(asteroids[i])
                i += 1
            else:
                for j in range(i + 1, n):
                    if -asteroids[j] >= asteroids[i]:
                        break
                else:
                    ans.extend(asteroids[i:])
                    return ans

                for k in range(j - 1, i - 1, -1):
                    if asteroids[k] > -asteroids[j]:
                        ans.extend(asteroids[i : k + 1])
                        break
                    elif asteroids[k] == -asteroids[j]:
                        ans.extend(asteroids[i:k])
                        break
                else:
                    ans.append(asteroids[j])
                i = j + 1
            # print(2, ans)
            # print(i, j)

        return ans

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = deque([])
        ans = []
        for a in asteroids:
            if a < 0 and not s:
                ans.append(a)
            elif a < 0 and s:
                while s and -a > s[-1]:
                    s.pop()
                if not s:
                    ans.append(a)
                else:
                    if s[-1] == -a:
                        s.pop()
            else:
                s.append(a)

        ans.extend(s)
        return ans
