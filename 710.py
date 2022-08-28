import random
from typing import List


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        # 太妙了, 为了每次采样都调用一次随机函数
        # 那么肯定是在一个范围内调用一次
        # 又怎么确定这个范围?[0:n)肯定不行
        # 又因为只有n-m个数, 在[0:n-m)好像更合适
        # 为了做到这一点可以把在这个范围内的黑名单中的数字映射到[n-m:n)中的不在黑名单中的数字
        m = len(blacklist)
        self.mid = cur = n - m
        blackSet = set(blacklist)
        self.mp = {}
        for i in blacklist:
            if i < self.mid:
                while cur in blackSet:
                    cur += 1
                self.mp[i] = cur
                cur += 1

    def pick(self) -> int:
        i = random.randrange(self.mid)
        if i in self.mp:
            return self.mp[i]
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
