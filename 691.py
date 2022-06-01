from collections import Counter, deque
from math import ceil
from typing import List


class Solution:
    def minStickers1(self, stickers: List[str], target: str) -> int:
        # 枚举
        target_cnter = Counter(target)
        n = len(stickers)

        # 过滤掉没有用的字母和sticker
        useful_stickers = []
        for i in range(n):
            tmp_cnter = Counter(c for c in stickers[i] if c in target_cnter)
            if len(tmp_cnter) > 0:
                flag = False
                for cnter in useful_stickers:
                    if all(k in cnter and cnter[k] >= v for k, v in tmp_cnter.items()):
                        flag = True
                        break
                if not flag:
                    useful_stickers.append(tmp_cnter)

        n = len(useful_stickers)
        ans = float("inf")

        def bfs(i, cnt, cur_cnter: Counter):
            nonlocal ans
            if cnt >= ans:
                return
            if all(v <= 0 for v in cur_cnter.values()):
                ans = min(ans, cnt)
                return
            if i == n:
                return
            max_cnt = 0
            for k, v in useful_stickers[i].items():
                if k in cur_cnter and cur_cnter[k] > 0:
                    max_cnt = max(max_cnt, ceil(cur_cnter[k] / v))
            for j in range(max_cnt + 1):
                new_cnter = {
                    k: v - (useful_stickers[i][k] if k in useful_stickers[i] else 0) * j
                    for k, v in cur_cnter.items()
                }
                bfs(i + 1, cnt + j, new_cnter)

        bfs(0, 0, target_cnter)
        return ans if ans != float("inf") else -1

    def minStickers2(self, stickers: List[str], target: str) -> int:
        # BFS
        n = len(stickers)
        # 过滤掉没有用的字母和sticker
        useful_stickers = []
        for i in range(n):
            tmp_cnter = Counter(c for c in stickers[i] if c in target)
            if len(tmp_cnter) > 0:
                for cnter in useful_stickers:
                    if all(k in cnter and cnter[k] >= v for k, v in tmp_cnter.items()):
                        break
                else:
                    useful_stickers.append(tmp_cnter)

        q = deque([(target, 0)])
        visit = {target}
        while q:
            cur, step = q.popleft()
            if not cur:
                return step
            for cnter in useful_stickers:
                # 优化, 优先拼出开头, 可以一定程度上避免重复
                # 比如说先删a后删b, 和先删b后删a一样, 我们在乎的是选了ab, 而不是排列ab
                # 参考https://leetcode.cn/problems/stickers-to-spell-word/solution/pythonjavajavascriptgo-by-himymben-43ik/
                if cur[0] in cnter:
                    nxt = cur
                    for k, v in cnter.items():
                        nxt = nxt.replace(k, '', v)
                    if nxt not in visit:
                        q.append((nxt, step + 1))
                        visit.add(nxt)
        return -1

    def minStickers(self, stickers: List[str], target: str) -> int:
        # DP
        n = len(stickers)
        m = len(target)
        dp = [float('inf')] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            for ss in stickers:
                newMask = mask
                for c in ss:
                    for j in range(m):
                        if (mask >> j) & 1 == 0 and target[j] == c:
                            newMask |= 1 << j
                            break
                if newMask != mask:
                    dp[newMask] = min(dp[newMask], dp[mask] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1


# stickers = ["with", "example", "science"]
# target = "thehat"

# stickers = ["notice", "possible"]
# target = "basicbasic"

stickers = ["these", "guess", "about", "garden", "him"]
target = "atomher"

# stickers = ["notice", "possible"]
# target = "basicbasic"

print(Solution().minStickers(stickers, target))
