from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbor(s):
            for i in range(4):
                # s[i] = str((int(s[i]) + 1) % 10)
                yield s[:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
                yield s[:i] + str((int(s[i]) - 1) % 10) + s[i+1:]
                # s[i] = str((int(s[i]) - 2) % 10)
                # yield s
        visited = set(deadends)
        if '0000' in visited:
            return -1
        q = collections.deque(['0000'])
        visited.add('0000')
        ans = 0
        while q:
            length = len(q)
            for _ in range(length):
                tmp = q.pop()
                if tmp == target:
                    return ans
                
                for n in neighbor(tmp):
                    if not n in visited:
                        q.appendleft(n)
                        visited.add(n)
            ans += 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888'))