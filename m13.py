from typing import List
import collections


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sumOfDigits(num1, num2):
            sum = 0
            while num1 > 0:
                sum += num1 % 10
                num1 //= 10
            while num2 > 0:
                sum += num2 % 10
                num2 //= 10
            return sum
        visited = [False] * (m * n)
        q = collections.deque()
        q.appendleft((0, 0))
        visited[0] = True
        count = 1
        while q:
            i, j = q.pop()
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                # print(x,y)
                if 0 <= x < m and 0 <= y < n and not visited[x*n + y] and sumOfDigits(x, y) <= k:
                    print(x, y)
                    q.appendleft((x, y))
                    visited[x*n + y] = True
                    count += 1
            print('---')
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.movingCount(3, 2, 17))
