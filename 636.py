from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        s = []
        ans = [0] * n

        for log in logs:
            idx, flag, time = log.split('.')
            idx, time = int(idx), int(time)
            if flag[0] == 's':
                if s:
                    ans[s[-1][0]] += time - s[-1][1]
                s.append([idx, time])
            else:
                ans[idx] += time - s[-1][1] + 1
                s.pop()
                if s:
                    s[-1][1] = time + 1
        return ans
