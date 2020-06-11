from typing import List
import collections


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = collections.deque([0])
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                tmp = stack.pop()
                ans[tmp] = i - tmp
            stack.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    l = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(l))
