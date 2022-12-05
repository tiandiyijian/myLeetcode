from collections import deque
from typing import List


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        def getArray() -> List[int]:
            return [0] * (n + 1)

        n = len(boxes)
        p, w, neg, W = getArray(), getArray(), getArray(), getArray()

        for i in range(1, n + 1):
            p[i], w[i] = boxes[i - 1]
            if i > 1:
                neg[i] = neg[i - 1] + (p[i - 1] != p[i])
            W[i] = W[i - 1] + w[i]

        opt = deque([0])
        f, g = getArray(), getArray()

        for i in range(1, n + 1):
            while i - opt[0] > maxBoxes or W[i] - W[opt[0]] > maxWeight:
                # 前面的先不满足条件
                opt.popleft()

            f[i] = g[opt[0]] + neg[i] + 2 # 队头元素最小

            if i < n:
                g[i] = f[i] - neg[i + 1]
                while opt and g[opt[-1]] >= g[i]:
                    # 把没有新添加元素更优的出队
                    # 保证该队列是单调递增队列
                    opt.pop()
                opt.append(i)

        return f[-1]
